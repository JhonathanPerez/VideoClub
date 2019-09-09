import wx
from wx import xrc
from controller.usercontroller import UserController


class EliminarUsuario(wx.Frame):

    def __init__(self, frame_father, id_user):
        super(EliminarUsuario, self).__init__()
        self.xml = xrc.XmlResource('../View/eliminar_usuario.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Eliminar_Usuario')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Eliminar_Usuario')
        self.nombre = xrc.XRCCTRL(self.panel, 'Textctrl_Nombre')
        self.apellido = xrc.XRCCTRL(self.panel, 'Textctr_Apellido')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.id_user = id_user
        self.frame_father = frame_father
        self.user_controller = UserController()
        self.button_eliminar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.eliminar_usuario, self.button_eliminar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_usuario()
        self.frame.Show()



    def cargar_datos_usuario(self):
        usuario = self.user_controller.get_user(self.id_user)
        self.nombre.SetValue(usuario.nombre)
        self.apellido.SetValue(usuario.apellido)
        self.username.SetValue(usuario.nombre_usuario)


    def eliminar_usuario(self, evt):
        if self.user_controller.delete_user(self.id_user):
            wx.MessageBox('El Usuario se elimino exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.frame_father.load_data_listctrl_user()
            self.frame.Close()

    def cancelar(self, evt):
        self.frame.Close()










