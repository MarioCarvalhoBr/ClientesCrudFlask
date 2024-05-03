from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import ClienteForm
from app.models import Cliente

@app.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)

@app.route('/add', methods=['GET', 'POST'])
def add_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        novo_cliente = Cliente(nome=form.nome.data, email=form.email.data)
        db.session.add(novo_cliente)
        db.session.commit()
        flash('Cliente adicionado com sucesso!')
        return redirect(url_for('index'))
    return render_template('add_cliente.html', form=form)

@app.route('/edit/<uuid:id>', methods=['GET', 'POST'])
def edit_cliente(id):
    cliente = Cliente.query.get_or_404(str(id))
    form = ClienteForm(obj=cliente, id=str(cliente.id))  # Garante que o ID esteja como string
    if form.validate_on_submit():
        cliente.nome = form.nome.data
        cliente.email = form.email.data
        db.session.commit()
        flash('Informações do cliente atualizadas com sucesso!')
        return redirect(url_for('index'))
    return render_template('edit_cliente.html', form=form)

@app.route('/delete/<id>')
def delete_cliente(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
