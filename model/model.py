from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Float, Text,Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:PEREZortega10@@localhost/tienda")
DeclarativeBase = declarative_base(engine)
metadata = DeclarativeBase.metadata

class Serie(DeclarativeBase):
    __tablename__ = "Series"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String(50))
    temporadas = Column("temporadas", Integer())
    genero = Column("genero", String(50))
    autor = Column("autor", String(50))
    imagen = Column("imagen", String(200))

    def __repr__(self):
        return "<Serie: %s>" % (self.titulo)


class VideoJuego(DeclarativeBase):
    __tablename__ = "Juegos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String(50))
    genero = Column("genero", String(50))
    compania= Column("compania", String(50))
    plataforma = Column("plataforma",String(50))
    imagen = Column("imagen", String(200))

    def __repr__(self):
        return "<Juego: %s %s>" % (self.titulo, self.genero)



class Usuario(DeclarativeBase):
    __tablename__ = "Usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column("username", String(50), unique=True)
    nombre = Column("nombre", String(50))
    apellido = Column("apellido", String(50))
    contrasena = Column("password", String(50))
    imagen = Column("imagen", String(200))

    def __repr__(self):
        return "<Usuario: %s>" % (self.nombre_usuario)


class Administrador(DeclarativeBase):
    __tablename__ = "Administrador"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column("username", String(50), unique=True)
    nombre = Column("nombre", String(50))
    apellido = Column("apellido", String(50))
    contrasena = Column("password", String(50))
    imagen = Column("imagen", String(200))

    def __repr__(self):
        return "<Administrador: %s>" % (self.nombre_usuario)


class ReservaSerie(DeclarativeBase):
    __tablename__ = "Reservas_Series"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"))
    serie_id = Column(Integer, ForeignKey("Series.id"))


class ReservaJuego(DeclarativeBase):
    __tablename__ = "Reservas_Juegos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"))
    juego_id = Column(Integer, ForeignKey("Juegos.id"))



metadata.create_all()