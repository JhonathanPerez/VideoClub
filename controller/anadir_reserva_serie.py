import wx
from wx import xrc
from controller.reserva_serie_controller import ReservaSerieController
from controller.usercontroller import UserController
from controller.seriecontroller import SerieController



class AnadirReservaSerie(wx.Frame):

    def __init__(self, frame_father):
        super(AnadirReservaSerie, self).__init__()
        self.xml = xrc.XmlResource('../View/anadir_reserva_serie.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Anadir_Reserva')
        self.panel = xrc.XRCCTRL(self.frame, 'AnadirReserva_Panel')
        self.id_cliente = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Cliente')
        self.id_serie = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Serie')
        self.button_anadir = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame_father = frame_father
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_reserva, self.button_anadir)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_frame, self.button_cancelar)
        self.reserva_serie_controller = ReservaSerieController()
        self.user_controller = UserController()
        self.serie_controller = SerieController()
        self.frame.Show()


    def anadir_reserva(self, evt):

        id_cliente = self.id_cliente.GetValue()
        id_serie = self.id_serie.GetValue()

        if id_cliente and id_serie:
            if self.user_controller.get_user(id_cliente) != None and self.serie_controller.get_serie(id_serie) != None:
                if self.reserva_serie_controller.search_booking(id_cliente, id_serie) == False:
                    if self.reserva_serie_controller.create_booking(id_cliente,id_serie):
                        wx.MessageBox('La reserva se creo con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                        self.frame_father.load_data_listctrl_serie()
                        self.frame.Close()
                else:
                    wx.MessageBox('Ya existe una reserva con los mismos datos ', 'Error', wx.OK | wx.ICON_ERROR)
                    self.limpiar_campos()
            else:
                wx.MessageBox('El usuario o la serie no existe en el sistema intente nuevamente', 'Error',
                              wx.OK | wx.ICON_ERROR)


        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)



    def limpiar_campos(self):
        self.id_cliente.Clear()
        self.id_serie.Clear()


    def cerrar_frame(self, evt):
        self.frame.Close()
