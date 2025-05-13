from flask_sqlalchemy import SQLAlchemy

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

# Modelo de la tabla Reserva
class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)
