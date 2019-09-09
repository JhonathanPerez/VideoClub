import wx
from wx import xrc
from controller.seriecontroller import SerieController


class ModificarSerie(wx.Frame):

    def __init__(self, frame_father, id_serie):
        super(ModificarSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/modificar_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Modificar_Serie')
        self.panel = xrc.XRCCTRL(self.frame, 'ModificarSerie_Panel')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_Titulo')
        self.genero = xrc.XRCCTRL(self.panel, 'Textctrl_Genero')
        self.autor = xrc.XRCCTRL(self.panel, 'Textctrl_Autor')
        self.temporadas = xrc.XRCCTRL(self.panel, 'Textctrl_Temporadas')
        self.imagen = xrc.XRCCTRL(self.panel, 'Filepicker_Imagen')
        self.id_serie = id_serie
        self.frame_father = frame_father
        self.serie_controller = SerieController()
        self.button_modificar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.modificar_serie, self.button_modificar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_serie()
        self.frame.Show()



    def cargar_datos_serie(self):
        serie = self.serie_controller.get_serie(self.id_serie)
        self.titulo.SetValue(serie.titulo)
        self.genero.SetValue(serie.genero)
        self.autor.SetValue(serie.autor)
        self.temporadas.SetValue(str(serie.temporadas))

    def modificar_serie(self, evt):
        titulo = self.titulo.GetValue()
        genero = self.genero.GetValue()
        autor = self.autor.GetValue()
        temporadas = self.temporadas.GetValue()
        imagen = self.imagen.GetPath()


        if titulo and genero and autor and temporadas :
            data = {'titulo': titulo, 'genero': genero, 'autor': autor,'temporadas':temporadas , "imagen": imagen}
            if self.serie_controller.edit_serie(self.id_serie, data):
                wx.MessageBox('La serie se modifico exitosamente', 'Information', wx.OK | wx.ICON_INFORMATION)
                self.frame_father.load_data_listctrl_serie()
                self.cargar_datos_serie()

        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def cancelar(self, evt):
        self.frame.Close()










