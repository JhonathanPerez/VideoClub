import wx
from wx import xrc
from controller.gamecontroller import GameController


class EliminarJuego(wx.Frame):

    def __init__(self, frame_father, id_juego):
        super(EliminarJuego, self).__init__()
        self.xml = xrc.XmlResource('../View/eliminar_juego.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Eliminar_Juego')
        self.panel = xrc.XRCCTRL(self.frame, 'EliminarJuego_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.compania = xrc.XRCCTRL(self.panel, 'Textctrl_Compania')
        self.plataforma = xrc.XRCCTRL(self.panel, 'Textctrl_Plataforma')
        self.id_juego = id_juego
        self.frame_father = frame_father
        self.game_controller = GameController()
        self.button_eliminar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.eliminar_juego, self.button_eliminar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_juego()
        self.frame.Show()



    def cargar_datos_juego(self):
        juego = self.game_controller.get_game(self.id_juego)
        self.titulo.SetValue(juego.titulo)
        self.genero.SetValue(juego.genero)
        self.compania.SetValue(juego.compania)
        self.plataforma.SetValue(juego.plataforma)


    def eliminar_juego(self, evt):
        if self.game_controller.delete_game(self.id_juego):
            wx.MessageBox('El Video Juego se elimino exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.frame_father.load_data_listctrl_juego()
            self.frame.Close()

    def cancelar(self, evt):
        self.frame.Close()










