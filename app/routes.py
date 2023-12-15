from flask import Blueprint, render_template, redirect, url_for, flash
from flask import request, jsonify
from .models import db, Persona
from flask_login import login_user
from flask_login import login_required



main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/cursos')
@login_required
def cursos():
    return render_template('cursos.html')

@main.route('/formulario')
def formulario():
    return render_template('formulario.html')

@main.route('/submit_form', methods=['POST'])
def submit_form():
    nombre=request.form.get('nombre')
    apellido=request.form.get('apellido')
    email=request.form.get('email')
    password=request.form.get('password')

    nueva_persona=Persona(nombre=nombre,
                          apellido=apellido,
                          email=email)
    nueva_persona.set_password(password)

    db.session.add(nueva_persona)
    db.session.commit()

    return render_template('exito.html')    

@main.route('/ver_registros')
def ver_registros():
    personas=Persona.query.all()
    return render_template('ver_registros.html',
                           personas=personas)




@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Persona.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.cursos'))

        flash('Credenciales incorrectas. Por favor, inténtalo de nuevo.', 'danger')

    return render_template('login.html')

@main.route('/eliminar_cuenta', methods=['GET', 'POST'])
@login_required
def eliminar_cuenta():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Persona.query.filter_by(email=email).first()

        if user and user.check_password(password):
            db.session.delete(user)
            db.session.commit()

            flash('Cuenta eliminada exitosamente')
            return redirect(url_for('main.index'))

        flash('Por favor, inténtalo de nuevo')

    return render_template('eliminar.html')