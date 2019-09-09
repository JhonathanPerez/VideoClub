import wx
from wx import xrc
from controller.usercontroller import UserController


class ModificarUsuario(wx.Frame):

    def __init__(self, frame_father, id_user):
        super(ModificarUsuario, self).__init__()
        self.xml = xrc.XmlResource('../View/modificar_cuenta_usuario.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Modificar_Cuenta_Usuario')
        self.panel = xrc.XRCCTRL(self.frame, 'ModificarCuenta_Panel')
        self.nombre = xrc.XRCCTRL(self.panel, 'Textctrl_Nombre')
        self.apellido = xrc.XRCCTRL(self.panel, 'Textctrl_Apellido')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.foto = xrc.XRCCTRL(self.panel, 'Filepicker_Foto')
        self.id_user = id_user
        self.frame_father = frame_father
        self.user_controller = UserController()
        self.button_modificar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.modificar_usuario, self.button_modificar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_usuario()
        self.frame.Show()



    def cargar_datos_usuario(self):
        usuario = self.user_controller.get_user(self.id_user)
        self.nombre.SetValue(usuario.nombre)
        self.apellido.SetValue(usuario.apellido)
        self.username.SetValue(usuario.nombre_usuario)
        self.password = usuario.contrasena

    def modificar_usuario(self, evt):
        nombre = self.nombre.GetValue()
        apellido = self.apellido.GetValue()
        username = self.username.GetValue()
        foto = self.foto.GetPath()


        if nombre and apellido and username:
            data = {'nombre': nombre, 'apellido': apellido, 'username': username,'password':self.password , "imagen": foto}
            if self.user_controller.edit_user(self.id_user, data):
                wx.MessageBox('El Usuario se modifico exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
                self.frame_father.load_data_listctrl_user()
                self.cargar_datos_usuario()

        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def cancelar(self, evt):
        self.frame.Close()










