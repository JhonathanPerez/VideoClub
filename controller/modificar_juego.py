import wx
from wx import xrc
from controller.gamecontroller import GameController


class ModificarJuego(wx.Frame):

    def __init__(self, frame_father, id_juego):
        super(ModificarJuego, self).__init__()
        self.xml = xrc.XmlResource('../View/modificar_juego.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Modificar_Juego')
        self.panel = xrc.XRCCTRL(self.frame, 'ModificarJuego_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.compania = xrc.XRCCTRL(self.panel, 'Textctrl_Compania')
        self.plataforma = xrc.XRCCTRL(self.panel, 'Textctrl_Plataforma')
        self.imagen = xrc.XRCCTRL(self.panel, 'Filepicker_Imagen')
        self.id_juego = id_juego
        self.frame_father = frame_father
        self.game_controller = GameController()
        self.button_modificar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.modificar_juego, self.button_modificar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_juego()
        self.frame.Show()



    def cargar_datos_juego(self):
        juego = self.game_controller.get_game(self.id_juego)
        self.titulo.SetValue(juego.titulo)
        self.genero.SetValue(juego.genero)
        self.compania.SetValue(juego.compania)
        self.plataforma.SetValue(juego.plataforma)

    def modificar_juego(self, evt):
        titulo = self.titulo.GetValue()
        genero = self.genero.GetValue()
        compania = self.compania.GetValue()
        plataforma = self.plataforma.GetValue()
        imagen = self.imagen.GetPath()

        if imagen == "":
            imagen = None


        if titulo and genero and compania and plataforma :
            data = {'titulo': titulo, 'genero': genero, 'compania': compania,'plataforma':plataforma , "imagen": imagen}
            if self.game_controller.edit_game(self.id_juego, data):
                wx.MessageBox('El Video Juego se modifico exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
                self.frame_father.load_data_listctrl_juego()
                self.cargar_datos_juego()

        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def cancelar(self, evt):
        self.frame.Close()










