from model.model import ReservaSerie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


class ReservaSerieController():

    def connect_database(self):
        engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def create_booking(self, id_usuario, id_serie):
        reserva = ReservaSerie(usuario_id = id_usuario, serie_id=id_serie)
        session = self.connect_database()
        session.add(reserva)
        session.commit()
        session.close()
        return True

    def get_booking(self, id):
        session = self.connect_database()

        try:
            reserva = session.query(ReservaSerie).filter_by(id=id).one()
            session.close()
            return reserva

        except (MultipleResultsFound, NoResultFound):
            return None

    def get_all_bookings(self):
        session = self.connect_database()
        reservas = session.query(ReservaSerie).all()
        session.close()
        return reservas


    def edit_booking(self, id_booking, data):
        session = self.connect_database()
        reserva = session.query(ReservaSerie).filter_by(id=id_booking).one()
        reserva.usuario_id = data['usuario_id']
        reserva.serie_id = data['serie_id']
        session.add(reserva)
        session.commit()
        session.close()
        return True

    def delete_booking(self, id_booking):
        session = self.connect_database()
        reserva = session.query(ReservaSerie).filter_by(id=id_booking).one()
        session.delete(reserva)
        session.commit()
        session.close()
        return True

    def search_booking(self, id_user, id_serie):
        session = self.connect_database()

        try:
            booking = session.query(ReservaSerie).filter_by(usuario_id=id_user, serie_id=id_serie).one_or_none()
            session.close()

            if booking is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False

