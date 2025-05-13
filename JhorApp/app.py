from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Configuración inicial
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Base de datos
db = SQLAlchemy(app)

# Modelo
class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(50), nullable=False)

# Crear tablas
with app.app_context():
    db.create_all()

# Ruta principal: muestra formulario y lista de reservas
@app.route('/')
def index():
    reservas = Reserva.query.all()
    return render_template('index.html', reservas=reservas)

# Ruta para registrar nueva reserva
@app.route('/reservar', methods=['POST'])
def reservar():
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    nueva_reserva = Reserva(nombre=nombre, fecha=fecha)
    db.session.add(nueva_reserva)
    db.session.commit()
    return redirect('/')

# Ruta para ver reservas como texto plano
@app.route('/ver_reservas')
def ver_reservas():
    reservas = Reserva.query.all()
    return "<br>".join([f"{r.id} - {r.nombre} - {r.fecha}" for r in reservas])

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)

