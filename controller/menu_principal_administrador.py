import wx
from wx import xrc
from controller.lista_administradores import ListaAdministrador
from controller.lista_usuarios import ListaUsuario
from controller.lista_series import ListaSerie
from controller.lista_juegos import ListaJuego
from controller.lista_reservas import ListaReserva




class MenuPrincipalAdministrador(wx.Frame):

    def __init__(self, username_admin):
        super(MenuPrincipalAdministrador, self).__init__()
        self.xml = xrc.XmlResource('../View/menu_principal_administrador.xml')
        self.frame = self.xml.LoadFrame(None, 'Menu_Principal_Admin')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Menu_Principal_Admin')
        self.administradores = xrc.XRCCTRL(self.panel, 'Button_Administradores')
        self.usuarios = xrc.XRCCTRL(self.panel, 'Button_Usuarios')
        self.series = xrc.XRCCTRL(self.panel, 'Button_Series')
        self.juegos = xrc.XRCCTRL(self.panel, 'Button_Juegos')
        self.reservas = xrc.XRCCTRL(self.panel, 'Button_Reservas')
        self.salir = xrc.XRCCTRL(self.panel, 'Button_Salir')
        self.username = username_admin
        self.label_administrador = xrc.XRCCTRL(self.panel, 'Static_Text_Administrador')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.visualizar_administradores, self.administradores)
        self.frame.Bind(wx.EVT_BUTTON, self.visualizar_usuarios , self.usuarios)
        self.frame.Bind(wx.EVT_BUTTON, self.visualizar_series, self.series)
        self.frame.Bind(wx.EVT_BUTTON, self.visualizar_juegos, self.juegos)
        self.frame.Bind(wx.EVT_BUTTON, self.visualizar_reservas, self.reservas)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_sesion, self.salir)
        self.set_label_admin()
        self.frame.Show()



    def cerrar_sesion(self, evt):
        self.frame.Close()


    def set_label_admin(self):
        self.label_administrador.SetLabel(self.username)


    def visualizar_administradores(self, evt):
        self.visualizar_administradores = ListaAdministrador()


    def visualizar_usuarios(self, evt):
        self.visualizar_usuarios = ListaUsuario()


    def visualizar_series(self, evt):
        self.visualizar_series = ListaSerie()


    def visualizar_juegos(self, evt):
        self.visualizar_juego = ListaJuego()


    def visualizar_reservas(self, evt):
        self.visualizar_reservas = ListaReserva()










