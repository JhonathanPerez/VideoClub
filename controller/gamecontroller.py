from model.model import VideoJuego
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


class GameController():

    def connect_database(self):
        engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def create_game(self, titulo, genero, compania, plataforma, imagen):
        game = VideoJuego(titulo=titulo,genero=genero,
                      compania=compania, plataforma=plataforma, imagen=imagen)
        session = self.connect_database()
        session.add(game)
        session.commit()
        session.close()
        return True

    def get_game(self, id):
        session = self.connect_database()

        try:
            game = session.query(VideoJuego).filter_by(id=id).one()
            session.close()
            return game

        except (MultipleResultsFound, NoResultFound):
            return None

    def get_all_games(self):
        session = self.connect_database()
        games = session.query(VideoJuego).all()
        session.close()
        return games


    def edit_game(self, id_game, data):
        session = self.connect_database()
        game = session.query(VideoJuego).filter_by(id=id_game).one()
        game.titulo = data['titulo']
        game.genero = data['genero']
        game.compania = data['compania']
        game.plataforma = data['plataforma']
        game.imagen = data['imagen']
        session.add(game)
        session.commit()
        session.close()
        return True

    def delete_game(self, id_game):
        session = self.connect_database()
        game = session.query(VideoJuego).filter_by(id=id_game).one()
        session.delete(game)
        session.commit()
        session.close()
        return True


    def buscar_juego(self, titulo):
        session = self.connect_database()

        try:
            game = session.query(VideoJuego).filter_by(titulo=titulo).one_or_none()
            session.close()

            if game is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False


    def buscar_imagen(self, id):
        session = self.connect_database()

        try:
            game = session.query(VideoJuego).filter_by(id=id).one_or_none()
            session.close()

            if game is not None:
                return game.imagen
            return False

        except MultipleResultsFound:
            session.close()
            return False