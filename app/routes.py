from app import app, db
from flask import render_template, redirect, url_for, request

from app.models import Cliente

@app.route('/')
def index():
    clientes = Cliente.query.all()
    return render_template('index.html', clientes=clientes)

@app.route('/add', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        novo_cliente = Cliente(nome=nome, email=email)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_cliente.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_cliente.html', cliente=cliente)

@app.route('/delete/<id>')
def delete_cliente(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
