import wx
from wx import xrc
from controller.admincontroller import AdminController
from controller.eliminar_administrador import EliminarAdministrador
from controller.crear_cuenta_administrador import CrearCuentaAdministrador
from controller.modificar_cuenta_administrador import ModificarAdministrador


ACTUALIZAR_ADMIN = "Modificar"
ELIMINAR_ADMIN = "Eliminar"


class ListaAdministrador(wx.Frame):

    def __init__(self, *args, **kw):
        super(ListaAdministrador, self).__init__(*args, **kw)
        self.xml = xrc.XmlResource('../View/lista_administradores.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Administradores')
        self.panel = xrc.XRCCTRL(self.frame, 'Panel_Administradores')
        self.button_anadir_admin = xrc.XRCCTRL(self.panel, 'Button_Anadir_Administrador')
        self.listctrl_administrador = xrc.XRCCTRL(self.panel, 'Listctrl_Administradores')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.list_admins = []
        self.admin_list = []
        self.admin_controller = AdminController()
        self.load_columns_listctrl_admin()
        self.load_data_listctrl_admin()
        self.frame.Bind(wx.EVT_LIST_ITEM_SELECTED, self.list_admin_selected, self.listctrl_administrador)
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_administrador, self.button_anadir_admin)
        self.frame.Show()

    def load_columns_listctrl_admin(self):
        self.listctrl_administrador.InsertColumn(0, "ID", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_administrador.InsertColumn(1, "Nombre", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_administrador.InsertColumn(2, "Apellido", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_administrador.InsertColumn(3, "UserName", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)
        self.listctrl_administrador.InsertColumn(4, "Url_Foto", format=wx.LIST_FORMAT_CENTER, width=wx.LIST_AUTOSIZE)

    def load_data_listctrl_admin(self):
        self.admin_list = self.admin_controller.get_all_admins()
        self.listctrl_administrador.DeleteAllItems()

        for admin in self.admin_list:
            self.listctrl_administrador.Append(
                [admin.id, admin.nombre, admin.apellido, admin.nombre_usuario, admin.imagen])

    def list_admin_selected(self, evt):
        current_item = evt.GetIndex()
        self.list_admins = self.admin_controller.get_all_admins()
        self.admin_selected = self.list_admins[current_item]
        menu = wx.Menu()
        id_item_menu_update = wx.NewId()
        id_item_menu_delete = wx.NewId()
        menu.Append(id_item_menu_update, ACTUALIZAR_ADMIN)
        menu.Append(id_item_menu_delete, ELIMINAR_ADMIN)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_admin, id=id_item_menu_update)
        self.frame.Bind(wx.EVT_MENU, self.popup_item_selected_admin, id=id_item_menu_delete)
        self.frame.PopupMenu(menu)
        menu.Destroy()

    def popup_item_selected_admin(self, evt):
        id_item = evt.GetId()
        menu = evt.GetEventObject()
        menu_item = menu.FindItemById(id_item)

        if menu_item.GetLabel() == ACTUALIZAR_ADMIN:
            self.modificar_administrador = ModificarAdministrador(self, self.admin_selected.id)


        elif menu_item.GetLabel() == ELIMINAR_ADMIN:
            self.eliminar_administrador = EliminarAdministrador(self, self.admin_selected.id)


    def anadir_administrador(self, evt):
        self.anadir_admin= CrearCuentaAdministrador(self)










