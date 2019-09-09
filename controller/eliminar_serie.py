import wx
from wx import xrc
from controller.seriecontroller import SerieController


class EliminarSerie(wx.Frame):

    def __init__(self, frame_father, id_serie):
        super(EliminarSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/eliminar_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Eliminar_Serie')
        self.panel = xrc.XRCCTRL(self.frame, 'EliminarSerie_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.autor = xrc.XRCCTRL(self.panel, 'Textctrl_Autor')
        self.temporadas = xrc.XRCCTRL(self.panel, 'Textctrl_Temporadas')
        self.id_serie = id_serie
        self.frame_father = frame_father
        self.serie_controller = SerieController()
        self.button_eliminar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.eliminar_serie, self.button_eliminar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_usuario()
        self.frame.Show()



    def cargar_datos_usuario(self):
        serie = self.serie_controller.get_serie(self.id_serie)
        self.titulo.SetValue(serie.titulo)
        self.genero.SetValue(serie.genero)
        self.autor.SetValue(serie.autor)
        self.temporadas.SetValue(str(serie.temporadas))


    def eliminar_serie(self, evt):
        if self.serie_controller.delete_serie(self.id_serie):
            wx.MessageBox('La serie se elimino exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.frame_father.load_data_listctrl_serie()
            self.frame.Close()

    def cancelar(self, evt):
        self.frame.Close()










