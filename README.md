# Projeto CrudClientes

## Descrição

CrudClientes é uma aplicação web desenvolvida em Flask para gerenciar informações de clientes. Os dados são armazenados em um banco de dados SQLite. A aplicação permite adicionar, editar, visualizar e excluir clientes.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em sua máquina. Esta aplicação foi desenvolvida utilizando Python 3.8 no Ubuntu.

## Instalação

### Clonar o Repositório

```bash
git clone https://github.com/seu_usuario/CrudClientes.git
cd CrudClientes
```

### Configurar Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependências

```bash
pip install flask flask_sqlalchemy
```
# Instalar SQLite para testes
```bash
pip install sqlite3
```

### Configuração

Certifique-se de que todas as dependências estão instaladas e o ambiente virtual está ativado.

### Inicializar o Banco de Dados

```bash
python init_db.py
```

## Execução

Para rodar a aplicação, utilize o seguinte comando:

```bash
python run.py
```

Acesse a aplicação em `http://127.0.0.1:5000/`.

## Funcionalidades

- **Adicionar Cliente:** Permite adicionar um novo cliente ao banco de dados.
- **Visualizar Clientes:** Lista todos os clientes cadastrados.
- **Editar Cliente:** Permite editar informações de um cliente existente.
- **Excluir Cliente:** Permite excluir um cliente do banco de dados.