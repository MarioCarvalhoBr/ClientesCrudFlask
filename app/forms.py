from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from app.models import Cliente, Produto
from wtforms import HiddenField

class ClienteForm(FlaskForm):
    id = HiddenField()  # Armazena o ID do cliente quando estiver editando
    nome = StringField('Nome', validators=[DataRequired(message="O campo nome é obrigatório.")])
    email = StringField('Email', validators=[DataRequired(message="O campo nome é obrigatório."), Email(message="Por favor, forneça um email válido.")])

    def validate_email(self, email):
        cliente = Cliente.query.filter_by(email=email.data).first()
        if cliente and str(cliente.id) != self.id.data:
            raise ValidationError('Este email já está cadastrado. Por favor, use um diferente.')

class ProdutoForm(FlaskForm):
    id = HiddenField()  # Armazena o ID do produto quando estiver editando
    nome = StringField('Nome', validators=[DataRequired(message="O campo nome é obrigatório.")])
    descricao = StringField('Descrição', validators=[DataRequired(message="O campo descrição é obrigatório.")])
    preco = StringField('Preço', validators=[DataRequired(message="O campo preço é obrigatório.")])

    def validate_preco(self, preco):
        try:
            preco = float(preco.data)
        except ValueError:
            raise ValidationError('Por favor, forneça um valor numérico para o preço.')
        if preco < 0:
            raise ValidationError('O preço não pode ser negativo.')
        


class CursoForm(FlaskForm):
    id = HiddenField()  # Armazena o ID do produto quando estiver editando
    nome = StringField('Nome', validators=[DataRequired(message="O campo nome é obrigatório.")])
    descricao = StringField('Descrição', validators=[DataRequired(message="O campo descrição é obrigatório.")])
    preco = StringField('Preço', validators=[DataRequired(message="O campo preço é obrigatório.")])

    def validate_preco(self, preco):
        try:
            preco = float(preco.data)
        except ValueError:
            raise ValidationError('Por favor, forneça um valor numérico para o preço.')
        if preco < 0:
            raise ValidationError('O preço não pode ser negativo.')
    