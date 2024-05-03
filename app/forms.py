from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError
from app.models import Cliente
from wtforms import HiddenField

class ClienteForm(FlaskForm):
    id = HiddenField()  # Armazena o ID do cliente quando estiver editando
    nome = StringField('Nome', validators=[DataRequired(message="O campo nome é obrigatório.")])
    email = StringField('Email', validators=[DataRequired(message="O campo nome é obrigatório."), Email(message="Por favor, forneça um email válido.")])

    def validate_email(self, email):
        cliente = Cliente.query.filter_by(email=email.data).first()
        if cliente and str(cliente.id) != self.id.data:
            raise ValidationError('Este email já está cadastrado. Por favor, use um diferente.')