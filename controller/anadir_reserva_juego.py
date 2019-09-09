import wx
from wx import xrc
from controller.reserva_game_controller import ReservaJuegoController
from controller.usercontroller import UserController
from controller.gamecontroller import GameController



class AnadirReservaJuego(wx.Frame):

    def __init__(self, frame_father):
        super(AnadirReservaJuego, self).__init__()
        self.xml = xrc.XmlResource('../View/anadir_reserva_juego.xml')
        self.frame = self.xml.LoadFrame(None, 'Frame_Anadir_Reserva_Juego')
        self.panel = xrc.XRCCTRL(self.frame, 'AnadirReserva_Panel')
        self.id_cliente = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Cliente')
        self.id_juego = xrc.XRCCTRL(self.panel, 'Textctrl_ID_Juego')
        self.button_anadir = xrc.XRCCTRL(self.panel, 'wxID_OK')
        self.button_cancelar = xrc.XRCCTRL(self.panel, 'wxID_CANCEL')
        self.frame.SetIcon(wx.Icon("../view/System_Images/icon.png"))
        self.frame_father = frame_father
        self.frame.Bind(wx.EVT_BUTTON, self.anadir_reserva, self.button_anadir)
        self.frame.Bind(wx.EVT_BUTTON, self.cerrar_frame, self.button_cancelar)
        self.reserva_juego_controller = ReservaJuegoController()
        self.user_controller = UserController()
        self.game_controller = GameController()
        self.frame.Show()


    def anadir_reserva(self, evt):

        id_cliente = self.id_cliente.GetValue()
        id_juego = self.id_juego.GetValue()

        if id_cliente and id_juego:
            if self.user_controller.get_user(id_cliente) != None and self.game_controller.get_game(id_juego) != None:
                if self.reserva_juego_controller.search_booking(id_cliente, id_juego) == False:
                    if self.reserva_juego_controller.create_booking(id_cliente,id_juego):
                        wx.MessageBox('La reserva se creo con exito', 'Information', wx.OK | wx.ICON_INFORMATION)
                        self.frame_father.load_data_listctrl_juego()
                        self.frame.Close()
                else:
                    wx.MessageBox('Ya existe una reserva con los mismos datos ', 'Error', wx.OK | wx.ICON_ERROR)
                    self.limpiar_campos()
            else:
                wx.MessageBox('El usuario o el juego no existe en el sistema intente nuevamente', 'Error',
                              wx.OK | wx.ICON_ERROR)


        else:
            wx.MessageBox('Todos los campos son obligatorios', 'Error', wx.OK | wx.ICON_ERROR)



    def limpiar_campos(self):
        self.id_cliente.Clear()
        self.id_juego.Clear()


    def cerrar_frame(self, evt):
        self.frame.Close()
