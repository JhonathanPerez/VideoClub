import wx
from wx import xrc
from controller.reserva_serie_controller import ReservaSerie
from controller.reserva_serie_controller import ReservaSerieController
from controller.reserva_game_controller import ReservaJuegoController
from controller.seriecontroller import SerieController
from controller.modificar_reserva_serie import ModificarReservaSerie
from controller.eliminar_reserva_serie import EliminarReservaSerie
from controller.anadir_reserva_serie import AnadirReservaSerie
from controller.anadir_reserva_juego import AnadirReservaJuego




ACTUALIZAR_RESERVA = "Modificar"
ELIMINAR_RESERVA = "Eliminar"
FILTRO_SERIES = "Series"
FILTRO_JUEGOS = "Juegos"


class ListaReserva(wx.Frame):

    def __init__(self, *args, **kw):
        super(ListaReserva, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/lista_reservas.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Reservas')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Reservas')
        self.button_anadir_reserva = xrc.XRCCTRL(self.panel, 'Button_Anadir_Reservas')
        self.combox = xrc.XRCCTRL(self.panel, 'Combox')
        self.button_filtrar = xrc.XRCCTRL(self.panel, 'Button_Filtrar')
        self.listctrl_reservas = xrc.XRCCTRL(self.panel, 'Listctrl_Reservas')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.list_reservas = []
        self.reservas_list = []
        self.reserva_serie_controller = ReservaSerieController()
        self.serie_controller = SerieController()
        self.reserva_juego_controller = ReservaJuegoController()
        self.frame.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_reserva_selected, self.listctrl_reservas)
        self.frame.Bind(wx.EVT_BUTTON, self.cargar_datos, self.button_filtrar)
        self.frame.Bind(wx.EVT_BUTTON, self.cargar_eventos, self.button_anadir_reserva)
        self.cargar_datos_inicial()
        self.frame.Show()



    def cargar_datos_inicial(self):
        self.load_columns_listctrl_reserva_serie()
        self.load_data_listctrl_serie()
        self.filtro = FILTRO_SERIES


    def cargar_datos(self, evt):
        self.filtro = self.combox.GetValue()

        if self.filtro == FILTRO_SERIES:
            self.listctrl_reservas.DeleteAllColumns()
            self.load_columns_listctrl_reserva_serie()
            self.load_data_listctrl_serie()

        else:
            self.listctrl_reservas.DeleteAllColumns()
            self.load_columns_listctrl_reserva_jeugo()
            self.load_data_listctrl_juego()
            self.filtro = FILTRO_JUEGOS


    def cargar_eventos(self, evt):
        if self.filtro == FILTRO_SERIES:
            self.frame.Bind(wx.EVT_BUTTON, self.anadir_reserva_serie, self.button_anadir_reserva)
            print(0)
            self.filtro = FILTRO_SERIES
        else:
            print(1)
            self.frame.Bind(wx.EVT_BUTTON, self.anadir_reserva_juego, self.button_anadir_reserva)
            self.filtro = FILTRO_JUEGOS




    def load_columns_listctrl_reserva_serie(self):
        self.listctrl_reservas.InsertColumn(0, "ID_Reserva", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_reservas.InsertColumn(1, "ID_Usuario", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_reservas.InsertColumn(2, "ID_Serie", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_serie(self):
        self.reservas_list= self.reserva_serie_controller.get_all_bookings()
        self.listctrl_reservas.DeleteAllItems()

        for reserva in self.reservas_list:
            self.listctrl_reservas.Append(
                [reserva.id, reserva.usuario_id, reserva.serie_id])


    def load_columns_listctrl_reserva_jeugo(self):
        self.listctrl_reservas.InsertColumn(0, "ID_Reserva", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_reservas.InsertColumn(1, "ID_Usuario", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_reservas.InsertColumn(2, "ID_Juego", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_juego(self):
        self.reservas_list= self.reserva_juego_controller.get_all_bookings()
        self.listctrl_reservas.DeleteAllItems()

        for reserva in self.reservas_list:
            self.listctrl_reservas.Append(
                [reserva.id, reserva.usuario_id, reserva.juego_id])


    def list_reserva_selected(self, evt):
        current_item = evt.GetIndex()

        if self.filtro == FILTRO_SERIES:
            self.list_reservas = self.reserva_serie_controller.get_all_bookings()
            self.reserva_serie_selected = self.list_reservas[current_item]
            menu = wx.Menu()
            id_item_menu_update = wx.NewId()
            id_item_menu_delete = wx.NewId()
            menu.Append(id_item_menu_update, ACTUALIZAR_RESERVA)
            menu.Append(id_item_menu_delete, ELIMINAR_RESERVA)
            self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_serie, id=id_item_menu_update)
            self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_serie, id=id_item_menu_delete)
            self.frame.PopupMenu(menu)
            menu.Destroy()

        else:
            self.list_reservas = self.reserva_juego_controller.get_all_bookings()
            self.reserva_juego_selected = self.list_reservas[current_item]
            menu = wx.Menu()
            id_item_menu_update = wx.NewId()
            id_item_menu_delete = wx.NewId()
            menu.Append(id_item_menu_update, ACTUALIZAR_RESERVA)
            menu.Append(id_item_menu_delete, ELIMINAR_RESERVA)
            self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_juego, id=id_item_menu_update)
            self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_juego, id=id_item_menu_delete)
            self.frame.PopupMenu(menu)
            menu.Destroy()


    def popup_item_selected_serie(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_RESERVA:
            self.modificar_reserva_serie = ModificarReservaSerie(self, self.reserva_serie_selected.id)


        elif menu_item.GetLabel() == ELIMINAR_RESERVA:
            self.eliminar_reserva_serie = EliminarReservaSerie(self, self.reserva_serie_selected.id)


    def popup_item_selected_juego(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_RESERVA:
            print("Johan Gay")


        elif menu_item.GetLabel() == ELIMINAR_RESERVA:
            print("Johan Gay")



    def anadir_reserva_serie(self, evt):
        anadir_reserva = AnadirReservaSerie(self)


    def anadir_reserva_juego(self, evt):
        anadir_reserva = AnadirReservaJuego(self)











