import wx
from wx import xrc
from controller.admincontroller import AdminController


class ModificarAdministrador(wx.Frame):

    def __init__(self, frame_father, id_admin):
        super(ModificarAdministrador, self).__init__()
        self.xml = xrc.XmlResource('../View/modificar_cuenta_administrador.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Modificar_Cuenta_Administrador')
        self.panel = xrc.XRCCTRL(self.frame, 'ModificarCuenta_Panel')
        self.nombre = xrc.XRCCTRL(self.panel, 'Textctrl_Nombre')
        self.apellido = xrc.XRCCTRL(self.panel, 'Textctrl_Apellido')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.foto = xrc.XRCCTRL(self.panel, 'Filepicker_Foto')
        self.id_admin = id_admin
        self.frame_father = frame_father
        self.admin_controller = AdminController()
        self.button_modificar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.modificar_administrador, self.button_modificar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_administrador()
        self.frame.Show()



    def cargar_datos_administrador(self):
        administrador = self.admin_controller.get_admin(self.id_admin)
        self.nombre.SetValue(administrador.nombre)
        self.apellido.SetValue(administrador.apellido)
        self.username.SetValue(administrador.nombre_usuario)
        self.password = administrador.contrasena


    def modificar_administrador(self, evt):
        nombre = self.nombre.GetValue()
        apellido = self.apellido.GetValue()
        username = self.username.GetValue()
        foto = self.foto.GetPath()


        if nombre and apellido and username:
            data = {'nombre': nombre, 'apellido': apellido, 'username': username,'password':self.password , "imagen": foto}
            if self.admin_controller.edit_admin(self.id_admin, data):
                wx.MessageBox('El Administrador se modifico exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
                self.frame_father.load_data_listctrl_admin()
                self.cargar_datos_administrador()

        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def cancelar(self, evt):
        self.frame.Close()










