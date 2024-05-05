from app import db
import uuid


class Cliente(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Cliente {self.nome}>'

class Produto(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Produto {self.nome}>'


class Curso(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Curso {self.nome}>'
