from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import ClienteForm, ProdutoForm, CursoForm
from app.models import Cliente, Produto, Curso

# ROUTES DEFAULT
@app.route('/')
def home():
    clientes = Cliente.query.all()
    produtos = Produto.query.all()
    cursos = Curso.query.all()

    total_clientes = len(clientes)
    total_produtos = len(produtos)
    total_cursos = len(cursos)
    return render_template('home.html', total_clientes=total_clientes, total_produtos=total_produtos, total_cursos=total_cursos)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# ROUTES CLIENTE: CRUD
@app.route('/cliente/list')
def cliente_list():
    clientes = Cliente.query.all()
    return render_template('cliente/list.html', clientes=clientes)

@app.route('/cliente/add', methods=['GET', 'POST'])
def cliente_add():
    form = ClienteForm()
    if form.validate_on_submit():
        novo_cliente = Cliente(nome=form.nome.data, email=form.email.data)
        db.session.add(novo_cliente)
        db.session.commit()
        flash('Cliente adicionado com sucesso!')
        return redirect(url_for('cliente_list'))
    return render_template('cliente/add.html', form=form)

@app.route('/cliente/edit/<uuid:id>', methods=['GET', 'POST'])
def cliente_edit(id):
    cliente = Cliente.query.get_or_404(str(id))
    form = ClienteForm(obj=cliente, id=str(cliente.id))  # Garante que o ID esteja como string
    if form.validate_on_submit():
        cliente.nome = form.nome.data
        cliente.email = form.email.data
        db.session.commit()
        flash('Informações do cliente atualizadas com sucesso!')
        return redirect(url_for('cliente_list'))
    return render_template('cliente/edit.html', form=form)

@app.route('/cliente/delete/<id>')
def cliente_delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('cliente_list'))


# ROUTES PRODUTO: CRUD
@app.route('/produto/list')
def produto_list():
    produtos = Produto.query.all()
    return render_template('produto/list.html', produtos=produtos)

@app.route('/produto/add', methods=['GET', 'POST'])
def produto_add():
    form = ProdutoForm()
    if form.validate_on_submit():
        novo_produto = Produto(nome=form.nome.data, descricao=form.descricao.data, preco=form.preco.data)
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto adicionado com sucesso!')
        return redirect(url_for('produto_list'))
    return render_template('produto/add.html', form=form)

@app.route('/produto/edit/<uuid:id>', methods=['GET', 'POST'])
def produto_edit(id):
    produto = Produto.query.get_or_404(str(id))
    form = ProdutoForm(obj=produto, id=str(produto.id))
    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = form.preco.data
        db.session.commit()
        flash('Informações do produto atualizadas com sucesso!')
        return redirect(url_for('produto_list'))
    return render_template('produto/edit.html', form=form)

@app.route('/produto/delete/<id>')
def produto_delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produto_list'))

# ROUTES CURSO: CRUD
@app.route('/curso/list')
def curso_list():
    cursos = Curso.query.all()
    return render_template('curso/list.html', cursos=cursos)

@app.route('/curso/add', methods=['GET', 'POST'])
def curso_add():
    form = CursoForm()
    if form.validate_on_submit():
        novo_curso = Curso(nome=form.nome.data, descricao=form.descricao.data, preco=form.preco.data)
        db.session.add(novo_curso)
        db.session.commit()
        flash('Curso adicionado com sucesso!')
        return redirect(url_for('curso_list'))
    return render_template('curso/add.html', form=form)

@app.route('/curso/edit/<uuid:id>', methods=['GET', 'POST'])
def curso_edit(id):
    curso = Curso.query.get_or_404(str(id))
    form = CursoForm(obj=curso, id=str(curso.id))
    if form.validate_on_submit():
        curso.nome = form.nome.data
        curso.descricao = form.descricao.data
        curso.preco = form.preco.data
        db.session.commit()
        flash('Informações do curso atualizadas com sucesso!')
        return redirect(url_for('curso_list'))
    return render_template('curso/edit.html', form=form)

@app.route('/curso/delete/<id>')
def curso_delete(id):
    curso = Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('curso_list'))
