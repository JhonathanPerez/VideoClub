from model.model import Serie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


class SerieController():

    def connect_database(self):
        engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def create_serie(self, titulo, temporadas, genero, autor, imagen):
        serie = Serie(titulo=titulo,temporadas=temporadas,genero=genero,
                      autor=autor,imagen=imagen)
        session = self.connect_database()
        session.add(serie)
        session.commit()
        session.close()
        return True

    def get_serie(self, id):
        session = self.connect_database()

        try:
            serie = session.query(Serie).filter_by(id=id).one()
            session.close()
            return serie

        except (MultipleResultsFound, NoResultFound):
            return None

    def get_all_series(self):
        session = self.connect_database()
        series = session.query(Serie).all()
        session.close()
        return series


    def edit_serie(self, id_serie, data):
        session = self.connect_database()
        serie = session.query(Serie).filter_by(id=id_serie).one()
        serie.titulo = data['titulo']
        serie.temporadas = data['temporadas']
        serie.genero = data['genero']
        serie.autor = data['autor']
        serie.imagen = data['imagen']
        session.add(serie)
        session.commit()
        session.close()
        return True

    def delete_serie(self, id_serie):
        session = self.connect_database()
        serie = session.query(Serie).filter_by(id=id_serie).one()
        session.delete(serie)
        session.commit()
        session.close()
        return True


    def buscar_serie(self, titulo):
        session = self.connect_database()

        try:
            serie = session.query(Serie).filter_by(titulo=titulo).one_or_none()
            session.close()

            if serie is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False


    def buscar_imagen(self, id):
        session = self.connect_database()

        try:
            serie = session.query(Serie).filter_by(id=id).one_or_none()
            session.close()

            if serie is not None:
                return serie.imagen
            return False

        except MultipleResultsFound:
            session.close()
            return False