import wx
from wx import xrc
from controller.usercontroller import UserController
from controller.crear_cuenta_usuario1 import CrearCuentaUsuario
from controller.modificar_cuenta_usuario import ModificarUsuario
from controller.eliminar_usuario import EliminarUsuario



ACTUALIZAR_USER = "Modificar"
ELIMINAR_USER = "Eliminar"


class ListaUsuario(wx.Frame):

    def __init__(self, *args, **kw):
        super(ListaUsuario, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/lista_usuarios.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Usuarios')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Usuarios')
        self.button_anadir_user = xrc.XRCCTRL(self.panel, 'Button_Anadir_Usuario')
        self.listctrl_usuario = xrc.XRCCTRL(self.panel, 'Listctrl_Usuarios')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.list_users = []
        self.user_list = []
        self.user_controller = UserController()
        self.load_columns_listctrl_user()
        self.load_data_listctrl_user()
        self.frame.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_user_selected, self.listctrl_usuario)
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_usuario , self.button_anadir_user)
        self.frame.Show()

    def load_columns_listctrl_user(self):
        self.listctrl_usuario.InsertColumn(0, "ID", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_usuario.InsertColumn(1, "Nombre", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_usuario.InsertColumn(2, "Apellido", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_usuario.InsertColumn(3, "UserName", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_usuario.InsertColumn(4, "Url_Foto", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_user(self):
        self.admin_list = self.user_controller.get_all_users()
        self.listctrl_usuario.DeleteAllItems()

        for user in self.admin_list:
            self.listctrl_usuario.Append(
                [user.id, user.nombre, user.apellido, user.nombre_usuario, user.imagen])

    def list_user_selected(self, evt):
        current_item = evt.GetIndex()
        self.list_users = self.user_controller.get_all_users()
        self.user_selected = self.list_users[current_item]
        menu = wx.Menu()
        id_item_menu_update = wx.NewId()
        id_item_menu_delete = wx.NewId()
        menu.Append(id_item_menu_update, ACTUALIZAR_USER)
        menu.Append(id_item_menu_delete, ELIMINAR_USER)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_user, id=id_item_menu_update)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_user, id=id_item_menu_delete)
        self.frame.PopupMenu(menu)
        menu.Destroy()

    def popup_item_selected_user(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_USER:
            self.actualizar_usuario = ModificarUsuario(self, self.user_selected.id)


        elif menu_item.GetLabel() == ELIMINAR_USER:
            self.eliminar_usuario = EliminarUsuario(self, self.user_selected.id)

    def anadir_usuario(self, evt):
        self.anadir_admin= CrearCuentaUsuario(self)










