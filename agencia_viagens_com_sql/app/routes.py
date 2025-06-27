from flask import Blueprint, render_template
from .models import Cliente, PacoteViagem, Reserva

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/clientes')
def clientes():
    lista = Cliente.query.all()
    return render_template('clientes.html', clientes=lista)

@main.route('/pacotes')
def pacotes():
    lista = PacoteViagem.query.all()
    return render_template('pacotes.html', pacotes=lista)

@main.route('/reservas')
def reservas():
    lista = Reserva.query.all()
    return render_template('reservas.html', reservas=lista)