from model.model import Administrador
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound


class AdminController():

    def connect_database(self):
        engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def create_admin(self, nombre, apellido, username, password,imagen):
        admin = Administrador(nombre=nombre, apellido=apellido, nombre_usuario=username,
                    contrasena=password,imagen=imagen)
        session = self.connect_database()
        session.add(admin)
        session.commit()
        session.close()
        return True

    def get_admin(self, id):
        session = self.connect_database()

        try:
            admin = session.query(Administrador).filter_by(id=id).one()
            session.close()
            return admin

        except (MultipleResultsFound, NoResultFound):
            return None

    def get_all_admins(self):
        session = self.connect_database()
        admins = session.query(Administrador).all()
        session.close()
        return admins

    def search_admin(self, username, password):
        session = self.connect_database()

        try:
            admin = session.query(Administrador).filter_by(nombre_usuario=username, contrasena=password).one_or_none()
            session.close()

            if admin is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False

    def edit_admin(self, id_admin, data):
        session = self.connect_database()
        admin = session.query(Administrador).filter_by(id=id_admin).one()
        admin.username = data['username']
        admin.nombre = data['nombre']
        admin.apellido = data['apellido']
        admin.password = data['password']
        admin.imagen = data['imagen']
        session.add(admin)
        session.commit()
        session.close()
        return True

    def delete_admin(self, id_admin):
        session = self.connect_database()
        admin = session.query(Administrador).filter_by(id=id_admin).one()
        session.delete(admin)
        session.commit()
        session.close()
        return True


    def buscar_admin(self, username):
        session = self.connect_database()

        try:
            admin = session.query(Administrador).filter_by(nombre_usuario=username).one_or_none()
            session.close()

            if admin is not None:
                return True
            return False

        except MultipleResultsFound:
            session.close()
            return False


    def buscar_imagen(self, id):
        session = self.connect_database()

        try:
            admin = session.query(Administrador).filter_by(id=id).one_or_none()
            session.close()

            if admin is not None:
                return admin.imagen
            return False

        except MultipleResultsFound:
            session.close()
            return False