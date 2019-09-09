import wx
from wx import xrc
from controller.seriecontroller import SerieController
from controller.anadir_serie import AnadirSerie
from controller.modificar_serie import ModificarSerie
from controller.eliminar_serie import EliminarSerie



ACTUALIZAR_SERIE = "Modificar"
ELIMINAR_SERIE = "Eliminar"


class ListaSerie(wx.Frame):

    def __init__(self, *args, **kw):
        super(ListaSerie, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/lista_series.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Series')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Series')
        self.button_anadir_serie = xrc.XRCCTRL(self.panel, 'Button_Anadir_Serie')
        self.listctrl_serie = xrc.XRCCTRL(self.panel, 'Listctrl_Series')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.list_series = []
        self.serie_list = []
        self.serie_controller = SerieController()
        self.load_columns_listctrl_serie()
        self.load_data_listctrl_serie()
        self.frame.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_serie_selected, self.listctrl_serie)
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_serie, self.button_anadir_serie)
        self.frame.Show()

    def load_columns_listctrl_serie(self):
        self.listctrl_serie.InsertColumn(0, "ID", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_serie.InsertColumn(1, "Titulo", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_serie.InsertColumn(2, "Temporadas", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_serie.InsertColumn(3, "Genero", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_serie.InsertColumn(4, "Autor", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_serie.InsertColumn(5, "Url_Imagen", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_serie(self):
        self.serie_list = self.serie_controller.get_all_series()
        self.listctrl_serie.DeleteAllItems()

        for serie in self.serie_list:
            self.listctrl_serie.Append(
                [serie.id, serie.titulo, serie.temporadas, serie.genero, serie.autor, serie.imagen])


    def list_serie_selected(self, evt):
        current_item = evt.GetIndex()
        self.list_series = self.serie_controller.get_all_series()
        self.serie_selected = self.list_series[current_item]
        menu = wx.Menu()
        id_item_menu_update = wx.NewId()
        id_item_menu_delete = wx.NewId()
        menu.Append(id_item_menu_update, ACTUALIZAR_SERIE)
        menu.Append(id_item_menu_delete, ELIMINAR_SERIE)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_serie, id=id_item_menu_update)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_serie, id=id_item_menu_delete)
        self.frame.PopupMenu(menu)
        menu.Destroy()

    def popup_item_selected_serie(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_SERIE:
            self.modificar_serie = ModificarSerie(self, self.serie_selected.id)


        elif menu_item.GetLabel() == ELIMINAR_SERIE:
            self.eliminar_serie = EliminarSerie(self, self.serie_selected.id)

    def anadir_serie(self, evt):
        self.anadir_serie= AnadirSerie(self)










