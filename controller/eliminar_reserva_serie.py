import wx
from wx import xrc
from controller.reserva_serie_controller import ReservaSerieController
from controller.usercontroller import UserController
from controller.seriecontroller import SerieController


class EliminarReservaSerie(wx.Frame):

    def __init__(self, frame_father, id_reserva):
        super(EliminarReservaSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/eliminar_reserva_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Eliminar_Reserva')
        self.panel = xrc.XRCCTRL(self.frame, 'EliminarReserva_Panel')
        self.id_reserva = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Reserva')
        self.id_cliente = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Cliente')
        self.username = xrc.XRCCTRL(self.panel, 'Textctrl_Username')
        self.id_serie = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Serie')
        self.titulo = xrc.XRCCTRL(self.panel, 'Textctrl_titulo_serie')
        self.id_booking = id_reserva
        self.frame_father = frame_father
        self.reserva_serie_controller = ReservaSerieController()
        self.user_controller = UserController()
        self.serie_controller = SerieController()
        self.button_eliminar = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame.Bind(wx.EVT_BUTTON, self.eliminar_reserva, self.button_eliminar)
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

    def eliminar_reserva(self, evt):
        if self.reserva_serie_controller.delete_booking(self.id_booking):
            wx.MessageBox('La reserva se eliminó correctamente', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.frame_father.load_data_listctrl_juego()
            self.frame.Close()

    def cancelar(self, evt):
        self.frame.Close()










