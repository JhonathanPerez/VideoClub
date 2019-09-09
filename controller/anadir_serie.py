import wx
from wx import xrc
from controller.seriecontroller import SerieController



class AnadirSerie(wx.Frame):

    def __init__(self, frame_father):
        super(AnadirSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/anadir_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Anadir_Serie')
        self.panel = xrc.XRCCTRL(self.frame, 'AnadirSerie_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.autor = xrc.XRCCTRL(self.panel, 'Textctrl_Autor')
        self.temporadas = xrc.XRCCTRL(self.panel, 'Textctrl_Temporadas')
        self.imagen = xrc.XRCCTRL(self.panel, 'Filepicker_Imagen')
        self.button_anadir = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame_father = frame_father
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_serie, self.button_anadir)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_frame, self.button_cancelar)
        self.serie_controller = SerieController()
        self.frame.Show()


    def anadir_serie(self, evt):

        titulo = self.titulo.GetValue()
        genero = self.genero.GetValue()
        autor = self.autor.GetValue()
        temporadas = self.temporadas.GetValue()
        imagen = self.imagen.GetPath()

        if imagen == "":
            imagen = None

        if titulo and genero and autor and temporadas:

            if self.serie_controller.buscar_serie(titulo) == False:
                if self.serie_controller.create_serie(titulo,temporadas,genero,autor,imagen):
                    wx.MessageBox('La serie se añadio con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                    self.limpiar_campos()
                    self.frame_father.load_data_listctrl_serie()
            else:
                msg = "La serie %s"%titulo +" ya existe ingrese otro diferente o valla a la opción modificar"
                wx.MessageBox(msg, 'Error', wx.OK | wx.ICON_ERROR)
                self.limpiar_usuario()

        else:
            wx.MessageBox('Todos los campos excepto la imagen deben ser completados', 'Error', wx.OK | wx.ICON_ERROR)



    def limpiar_usuario(self):
        self.titulo.Clear()

    def limpiar_campos(self):
        self.titulo.Clear()
        self.genero.Clear()
        self.autor.Clear()
        self.temporadas.Clear()


    def cerrar_frame(self, evt):
        self.frame.Close()
