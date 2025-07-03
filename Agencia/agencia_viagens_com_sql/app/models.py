from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    Pagamento = db.relationship('Pagamento', backref='cliente', lazy=True)

class PacoteViagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    duracao_dias = db.Column(db.Integer)
    Pagamento = db.relationship('pagamento', backref='pacote', lazy=True)

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    pacote_id = db.Column(db.Integer, db.ForeignKey('pacotes.id'), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)