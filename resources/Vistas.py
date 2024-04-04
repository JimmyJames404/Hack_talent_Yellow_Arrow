from sqlalchemy import Column, Integer, String, Date, Time, DECIMAL, Enum, func
from db import db

class BoletosPorMes(db.Model):
    __tablename__ = 'BoletosPorMes'
    
    Mes = Column(Integer, primary_key=True)
    TotalBoletos = Column(Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class HistorialViajes(db.Model):
    __tablename__ = 'HistorialViajes'

    Pasajero = Column(String(100), primary_key=True)
    Viaje = Column(String(100), primary_key=True)
    Fecha = Column(Date)
    Horario = Column(Time)
    Fecha_compra = Column(Date)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class AnalisisViajes(db.Model):
    __tablename__ = 'AnalisisViajes'

    Viaje = Column(String(100), primary_key=True)
    Origen = Column(String(100))
    Destino = Column(String(100))
    Autobus = Column(String(100))
    Pasajero = Column(String(100))

    @classmethod
    def get_all(cls):
        return cls.query.all()


class PasajerosPorViaje(db.Model):
    __tablename__ = 'PasajerosPorViaje'

    Viaje = Column(String(100), primary_key=True)
    Pasajero = Column(String(100), primary_key=True)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class AsientosOcupados(db.Model):
    __tablename__ = 'AsientosOcupados'

    Viaje = Column(String(100), primary_key=True)
    AsientosOcupados = Column(Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class RutasDelDia(db.Model):
    __tablename__ = 'RutasDelDia'

    Viaje = Column(String(100), primary_key=True)
    Origen = Column(String(100))
    Destino = Column(String(100))
    Fecha = Column(Date)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class IngresosPorMes(db.Model):
    __tablename__ = 'IngresosPorMes'

    Mes = Column(Integer, primary_key=True)
    TotalIngresos = Column(DECIMAL(10, 2))

    @classmethod
    def get_all(cls):
        return cls.query.all()


class OcupacionPromedio(db.Model):
    __tablename__ = 'OcupacionPromedio'

    Viaje = Column(String(100), primary_key=True)
    OcupacionPromedio = Column(Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class PasajerosPorAutobus(db.Model):
    __tablename__ = 'PasajerosPorAutobus'

    ID_Autobus = Column(Integer, primary_key=True)
    Autobus = Column(String(100))
    Pasajero = Column(String(100))

    @classmethod
    def get_all(cls):
        return cls.query.all()


class BoletosPorTipoAsiento(db.Model):
    __tablename__ = 'BoletosPorTipoAsiento'

    Tipo_asiento = Column(Enum('Ventana', 'Pasillo'), primary_key=True)
    TotalBoletos = Column(Integer)

    @classmethod
    def get_all(cls):
        return cls.query.all()


class ChoferesPorAutobus(db.Model):
    __tablename__ = 'ChoferesPorAutobus'

    ID_Autobus = Column(Integer, primary_key=True)
    Autobus = Column(String(100))
    Chofer = Column(String(100))

    @classmethod
    def get_all(cls):
        return cls.query.all()
