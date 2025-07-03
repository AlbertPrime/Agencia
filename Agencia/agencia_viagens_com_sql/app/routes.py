from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Cliente, PacoteViagem, Pagamento
from . import db
from werkzeug.security import generate_password_hash


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')


# CLIENTES — GET + POST
@main.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')

        if not nome or not email or not senha:
            flash('Preencha todos os campos obrigatórios!')
            return redirect(url_for('main.clientes'))

        senha_hash = generate_password_hash(senha)

        novo_cliente = Cliente(
            nome=nome,
            email=email,
            senha=senha_hash,
            telefone=telefone
        )
        db.session.add(novo_cliente)
        db.session.commit()

        flash('Cliente cadastrado com sucesso!')
        return redirect(url_for('main.clientes'))

    lista = Cliente.query.all()
    return render_template('clientes.html', clientes=lista)

# PACOTES — GET + POST
@main.route('/pacotes', methods=['GET', 'POST'])
def pacotes():
    if request.method == 'POST':
        destino = request.form.get('destino')
        preco = request.form.get('preco')
        duracao = request.form.get('duracao_dias')

        if not destino or not preco:
            flash('Preencha todos os campos.')
            return redirect(url_for('main.pacotes'))

        novo = PacoteViagem(destino=destino, preco=float(preco), duracao_dias=int(duracao))
        db.session.add(novo)
        db.session.commit()

        flash('Pacote cadastrado com sucesso!')
        return redirect(url_for('main.pacotes'))

    lista = PacoteViagem.query.all()
    return render_template('pacotes.html', pacotes=lista)


# PAGAMENTO — GET + POST
@main.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')
        pacote_id = request.form.get('pacote_id')
        data_reserva = request.form.get('data_reserva')

        if not cliente_id or not pacote_id or not data_reserva:
            flash('Preencha todos os campos.')
            return redirect(url_for('main.pagamento'))

        novo = Pagamento(cliente_id=int(cliente_id), pacote_id=int(pacote_id), data_reserva=data_reserva)
        db.session.add(novo)
        db.session.commit()

        flash('Pagamento registrado com sucesso!')
        return redirect(url_for('main.pagamento'))

    lista = Pagamento.query.all()
    return render_template('pagamento.html', pagamento=lista)
