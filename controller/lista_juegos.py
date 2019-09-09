import wx
from wx import xrc
from controller.gamecontroller import GameController
from controller.anadir_juego import AnadirJuego
from controller.modificar_juego import ModificarJuego
from controller.eliminar_juego import EliminarJuego



ACTUALIZAR_JUEGO = "Modificar"
ELIMINAR_JUEGO = "Eliminar"


class ListaJuego(wx.Frame):

    def __init__(self, *args, **kw):
        super(ListaJuego, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/lista_juegos.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Juegos')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Juegos')
        self.button_anadir_juego = xrc.XRCCTRL(self.panel, 'Button_Anadir_Juego')
        self.listctrl_juego = xrc.XRCCTRL(self.panel, 'Listctrl_Juegos')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.list_juegos = []
        self.game_list = []
        self.game_controller = GameController()
        self.load_columns_listctrl_juego()
        self.load_data_listctrl_juego()
        self.frame.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_juego_selected, self.listctrl_juego)
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_juego, self.button_anadir_juego)
        self.frame.Show()

    def load_columns_listctrl_juego(self):
        self.listctrl_juego.InsertColumn(0, "ID", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_juego.InsertColumn(1, "Titulo", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_juego.InsertColumn(3, "Genero", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_juego.InsertColumn(4, "Compañia", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_juego.InsertColumn(5, "Plataforma", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_juego.InsertColumn(6, "Url_Imagen", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_juego(self):
        self.game_list = self.game_controller.get_all_games()
        self.listctrl_juego.DeleteAllItems()

        for game in self.game_list:
            self.listctrl_juego.Append(
                [game.id, game.titulo, game.genero, game.compania, game.plataforma, game.imagen])


    def list_juego_selected(self, evt):
        current_item = evt.GetIndex()
        self.list_juegos = self.game_controller.get_all_games()
        self.game_selected = self.list_juegos[current_item]
        menu = wx.Menu()
        id_item_menu_update = wx.NewId()
        id_item_menu_delete = wx.NewId()
        menu.Append(id_item_menu_update, ACTUALIZAR_JUEGO)
        menu.Append(id_item_menu_delete, ELIMINAR_JUEGO)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_juego, id=id_item_menu_update)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_juego, id=id_item_menu_delete)
        self.frame.PopupMenu(menu)
        menu.Destroy()

    def popup_item_selected_juego(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_JUEGO:
            self.modificar_juego = ModificarJuego(self, self.game_selected.id)


        elif menu_item.GetLabel() == ELIMINAR_JUEGO:
            self.eliminar_juego = EliminarJuego(self, self.game_selected.id)

    def anadir_juego(self, evt):
        self.anadir_juego = AnadirJuego(self)










