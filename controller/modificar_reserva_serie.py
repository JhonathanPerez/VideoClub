import wx
from wx import xrc
from controller.reserva_serie_controller import ReservaSerieController
from controller.seriecontroller import SerieController
from controller.usercontroller import UserController


class ModificarReservaSerie(wx.Frame):

    def __init__(self, frame_father, id_reserva):
        super(ModificarReservaSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/modificar_reserva_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Modificar_Reserva')
        self.panel = xrc.XRCCTRL(self.frame, 'ModificarReserva_Panel')
        self.id_reserva = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Reserva')
        self.id_cliente = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Cliente')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.id_serie = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Serie')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_titulo_serie')
        self.id_booking= id_reserva
        self.frame_father = frame_father
        self.reserva_serie_controller = ReservaSerieController()
        self.serie_controller = SerieController()
        self.user_controller = UserController()
        self.button_modificar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.modificar_serie, self.button_modificar)
        self.frame.Bind(wx.EVT_BUTTON, self.cancelar, self.button_cancelar)
        self.cargar_datos_reserva()
        self.frame.Show()



    def cargar_datos_reserva(self):

        reserva = self.reserva_serie_controller.get_booking(self.id_booking)
        serie = self.serie_controller.get_serie(reserva.serie_id)
        user = self.user_controller.get_user(reserva.usuario_id)
        self.id_reserva.SetValue(str(reserva.id))
        self.id_cliente.SetValue(str(user.id))
        self.username.SetValue(user.nombre_usuario)
        self.id_serie.SetValue(str(serie.id))
        self.titulo.SetValue(serie.titulo)


    def modificar_serie(self, evt):
        id_cliente = self.id_cliente.GetValue()
        id_serie = self.id_serie.GetValue()

        if id_cliente and id_serie:
            if self.user_controller.get_user(id_cliente) != None and self.serie_controller.get_serie(id_serie) != None:
                data = {"usuario_id":id_cliente, "serie_id":id_serie}
                if self.reserva_serie_controller.edit_booking(self.id_booking, data):
                    wx.MessageBox('La reserva se modificó con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                    self.frame_father.load_data_listctrl_serie()
                    self.frame.Close()

            else:
                wx.MessageBox('El usuario o la serie no existe en el sistema intente nuevamente', 'Error', wx.OK | wx.ICON_ERROR)


        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)

    def cancelar(self, evt):
        self.frame.Close()










