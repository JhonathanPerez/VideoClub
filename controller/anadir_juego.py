import wx
from wx import xrc
from controller.gamecontroller import GameController



class AnadirJuego(wx.Frame):

    def __init__(self, frame_father):
        super(AnadirJuego, self).__init__()
        self.xml = xrc.XmlResource('../View/anadir_juego.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Anadir_Juego')
        self.panel = xrc.XRCCTRL(self.frame, 'AnadirJuego_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.compania = xrc.XRCCTRL(self.panel, 'Textctrl_Compania')
        self.plataforma = xrc.XRCCTRL(self.panel, 'Textctrl_Plataforma')
        self.imagen = xrc.XRCCTRL(self.panel, 'Filepicker_Imagen')
        self.button_anadir = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame_father = frame_father
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_juego, self.button_anadir)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_frame, self.button_cancelar)
        self.game_controller = GameController()
        self.frame.Show()


    def anadir_juego(self, evt):

        titulo = self.titulo.GetValue()
        genero = self.genero.GetValue()
        compania = self.compania.GetValue()
        plataforma = self.plataforma.GetValue()
        imagen = self.imagen.GetPath()

        if imagen == "":
            imagen = None

        if titulo and genero and compania and plataforma:

            if self.game_controller.buscar_juego(titulo) == False:
                if self.game_controller.create_game(titulo,genero,compania,plataforma,imagen):
                    wx.MessageBox('EL Video Juego se añadio con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                    self.limpiar_campos()
                    self.frame_father.load_data_listctrl_juego()
            else:
                msg = "El Video Juego %s"%titulo +" ya existe ingrese otro diferente o valla a la opción modificar"
                wx.MessageBox(msg, 'Error', wx.OK | wx.ICON_ERROR)
                self.limpiar_titulo()

        else:
            wx.MessageBox('Todos los campos excepto la imagen deben ser completados', 'Error', wx.OK | wx.ICON_ERROR)



    def limpiar_titulo(self):
        self.titulo.Clear()

    def limpiar_campos(self):
        self.titulo.Clear()
        self.genero.Clear()
        self.compania.Clear()
        self.plataforma.Clear()


    def cerrar_frame(self, evt):
        self.frame.Close()
