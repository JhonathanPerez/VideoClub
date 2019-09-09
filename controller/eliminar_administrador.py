import wx
from wx import xrc
from controller.admincontroller import AdminController


class EliminarAdministrador(wx.Frame):

    def __init__(self, frame_father, id_admin):
        super(EliminarAdministrador, self).__init__()
        self.xml = xrc.XmlResource('../View/eliminar_administrador.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Eliminar_Administrador')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Eliminar_Administrador')
        self.nombre = xrc.XRCCTRL(self.panel, 'Textctrl_Nombre_Administrador')
        self.apellido = xrc.XRCCTRL(self.panel, 'Textctr_Apellido_Administrador')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username_Administrador')
        self.id_admin = id_admin
        self.frame_father = frame_father
        self.admin_controller = AdminController()
        self.button_eliminar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.eliminar_administrador, self.button_eliminar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_administrador()
        self.frame.Show()



    def cargar_datos_administrador(self):
        administrador = self.admin_controller.get_admin(self.id_admin)
        self.nombre.SetValue(administrador.nombre)
        self.apellido.SetValue(administrador.apellido)
        self.username.SetValue(administrador.nombre_usuario)


    def eliminar_administrador(self, evt):
        if self.admin_controller.delete_admin(self.id_admin):
            wx.MessageBox('El Administrador se elimino exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.frame_father.load_data_listctrl_admin()
            self.frame.Close()

    def cancelar(self, evt):
        self.frame.Close()










