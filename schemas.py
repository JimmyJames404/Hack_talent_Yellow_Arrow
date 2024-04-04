from marshmallow import Schema, fields


# Definición de esquema para la tabla Estacion
class EstacionSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    direccion = fields.Str()
    latitud = fields.Decimal(as_string=True)
    longitud = fields.Decimal(as_string=True)
    andenes = fields.Int()
    telefonos = fields.Str()
    capacidad = fields.Int()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Viajes
class ViajesSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    origen = fields.Int()
    destino = fields.Int()
    precio = fields.Decimal(as_string=True)
    tiempo_estimado = fields.Int()
    fecha = fields.Date()
    horario = fields.Time()
    capacidad_autobus = fields.Int()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Ubicaciones_Sede
class UbicacionesSedeSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    latitud = fields.Decimal(as_string=True)
    longitud = fields.Decimal(as_string=True)
    direccion = fields.Str()
    telefono = fields.Str()
    capacidad = fields.Int()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Paradas
class ParadasSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    latitud = fields.Decimal(as_string=True)
    longitud = fields.Decimal(as_string=True)
    direccion = fields.Str()
    capacidad = fields.Int()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Autobuses
class AutobusesSchema(Schema):
    id = fields.Int(dump_only=True)
    modelo = fields.Str()
    ubicacion_actual = fields.Int()
    capacidad = fields.Int()
    asientos_disponibles = fields.Int()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Asientos
class AsientosSchema(Schema):
    id = fields.Int(dump_only=True)
    asiento = fields.Str(required=True)
    formacion_autobus = fields.Int()
    tipo_asiento = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Pasajeros
class PasajerosSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    edad = fields.Int()
    fecha_nacimiento = fields.Date()
    curp = fields.Str()
    correo_electronico = fields.Email()
    numero_telefonico = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Choferes
class ChoferesSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    licencia_conducir = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)

# Definición de esquema para la tabla Boletos
class BoletosSchema(Schema):
    id = fields.Int(dump_only=True)
    asiento_pasajero = fields.Int()
    id_pasajero = fields.Int()
    id_autobus = fields.Int()
    id_viaje = fields.Int()
    fecha_compra = fields.DateTime(dump_only=True)
    precio = fields.Decimal(as_string=True)
    estatus_pago = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
    ultima_actualizacion = fields.DateTime(dump_only=True)
