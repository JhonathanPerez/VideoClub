import wx
from wx import xrc
from controller.admincontroller import AdminController


class CrearCuentaAdministrador(wx.Frame):

    def __init__(self, frame_father):
        super(CrearCuentaAdministrador, self).__init__()
        self.xml = xrc.XmlResource('../View/crear_cuenta_administrador.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Crear_Cuenta_Administrador')
        self.panel = xrc.XRCCTRL(self.frame, 'CrearCuenta_Panel')
        self.nombre = xrc.XRCCTRL(self.panel, 'Textctrl_Nombre')
        self.apellido = xrc.XRCCTRL(self.panel, 'Textctrl_Apellido')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.password = xrc.XRCCTRL(self.panel, 'Textctrl_Password')
        self.foto = xrc.XRCCTRL(self.panel, 'Filepicker_Foto')
        self.button_crear = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame_father = frame_father
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.crear_administrador, self.button_crear)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_frame, self.button_cancelar)
        self.admin_controller = AdminController()
        self.frame.Show()


    def crear_administrador(self, evt):

        nombre = self.nombre.GetValue()
        apellido = self.apellido.GetValue()
        username = self.username.GetValue()
        password = self.password.GetValue()
        foto = self.foto.GetPath()

        if foto == "":
            foto = None

        if nombre and apellido and username and password:

            if self.admin_controller.buscar_admin(username) == False:
                if self.admin_controller.create_admin(nombre, apellido, username, password, foto):
                    wx.MessageBox('El Administrador se creo con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                    self.limpiar_campos()
                    self.frame_father.load_data_listctrl_admin()
            else:
                msg = "El nombre de usuario %s"%username +" ya existe ingrese otro diferente"
                wx.MessageBox(msg, 'Error', wx.OK | wx.ICON_ERROR)
                self.limpiar_usuario()

        else:
            wx.MessageBox('Todos los campos excepto la foto deben ser completados', 'Error', wx.OK | wx.ICON_ERROR)



    def limpiar_usuario(self):
        self.username.Clear()

    def limpiar_campos(self):
        self.nombre.Clear()
        self.apellido.Clear()
        self.username.Clear()
        self.password.Clear()


    def cerrar_frame(self, evt):
        self.frame.Close()
