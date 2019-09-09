from model.model import Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


class UserController():

    def connect_database(self):
        engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def create_user(self, nombre, apellido, username, password, imagen):
        usuario = Usuario(nombre=nombre, apellido=apellido, nombre_usuario=username,
                    contrasena=password, imagen =imagen)
        session = self.connect_database()
        session.add(usuario)
        session.commit()
        session.close()
        return True

    def edit_user(self, id_user, data):
        session = self.connect_database()
        user = session.query(Usuario).filter_by(id=id_user).one()
        user.username = data['username']
        user.nombre = data['nombre']
        user.apellido = data['apellido']
        user.password = data['password']
        user.imagen = data['imagen']
        session.add(user)
        session.commit()
        session.close()
        return True

    def delete_user(self, id_user):
        session = self.connect_database()
        user = session.query(Usuario).filter_by(id=id_user).one()
        session.delete(user)
        session.commit()
        session.close()
        return True


    def get_user(self, id):
        session = self.connect_database()

        try:
            user = session.query(Usuario).filter_by(id=id).one()
            session.close()
            return user

        except (MultipleResultsFound, NoResultFound):
            return None

    def get_all_users(self):
        session = self.connect_database()
        users = session.query(Usuario).all()
        session.close()
        return users

    def buscar_usuario(self, username):
        session = self.connect_database()

        try:
            user = session.query(Usuario).filter_by(nombre_usuario=username).one_or_none()
            session.close()

            if user is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False


    def search_user(self, username, password):
        session = self.connect_database()

        try:
            user = session.query(Usuario).filter_by(nombre_usuario=username, contrasena=password).one_or_none()
            session.close()

            if user is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False


    def buscar_imagen(self, id):
        session = self.connect_database()

        try:
            user = session.query(Usuario).filter_by(id=id).one_or_none()
            session.close()

            if user is not None:
                return user.imagen
            return False

        except MultipleResultsFound:
            session.close()
            return False