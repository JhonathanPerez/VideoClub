import wx
from wx import xrc
from controller.crear_cuenta_usuario import CrearCuentaUsuario
from controller.menu_principal_administrador import MenuPrincipalAdministrador
from controller.usercontroller import UserController
from controller.admincontroller import AdminController



class LoginFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(LoginFrame, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/Login.xml')
        self.frame = self.xml.LoadFrame(None, 'Login_Frame')
        self.panel = xrc.XRCCTRL(self.frame, 'Login_Panel')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Usuario')
        self.password = xrc.XRCCTRL(self.panel, 'Textctrl_Contrasena')
        self.button_ingresar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_ccuenta = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.validate_user, self.button_ingresar)
        self.frame.Bind(wx.EVT_BUTTON, self.crear_cuenta, self.button_ccuenta)
        self.user_controller = UserController()
        self.admin_controller = AdminController()
        self.frame.Show()

    def validate_user(self, evt):
        username = self.username.GetValue()
        password = self.password.GetValue()

        if username and password:
            if self.user_controller.search_user(username, password):
                self.frame.Close()
                wx.MessageBox('Eres un Usuario', 'Error', wx.OK | wx.ICON_ERROR)
            elif self.admin_controller.search_admin(username, password):
                self.frame.Close()
                self.menu_admin = MenuPrincipalAdministrador(username)

            else:
                wx.MessageBox('Datos incorrectos o usuario no registrado', 'Error', wx.OK | wx.ICON_ERROR)



        else:
            wx.MessageBox('Todos Los Campos Son Obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def crear_cuenta(self, evt):
        self.crear_cuenta = CrearCuentaUsuario()







if __name__ == '__main__':
    app = wx.App()
    frame = LoginFrame()
    app.MainLoop()
