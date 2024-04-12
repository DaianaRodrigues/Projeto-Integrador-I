# app.py - Exemplo de aplicativo Flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurando o banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Dr110594*180@localhost/Gestao_de_Salao'
# Substitua 'username', 'password' e 'databasename' pelas suas credenciais e nome do banco de dados MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definição do modelo de dados
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100))
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'))
    servico = db.relationship('Servico', backref=db.backref('agendamentos', lazy=True))

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)

# Simulando um banco de dados simples com uma lista de dicionários
servicos = [
    {'id': 1, 'nome': 'Corte de Cabelo', 'preco': 50},
    {'id': 2, 'nome': 'Manicure', 'preco': 30},
    {'id': 3, 'nome': 'Massagem', 'preco': 80}
]

# Rota para a página inicial que lista os serviços
@app.route('/')
def index():
    return render_template('index.html', servicos=servicos)

# Rota para agendar um serviço
@app.route('/agendar/<int:servico_id>', methods=['GET', 'POST'])
def agendar(servico_id):
    servico = Servico.query.get(servico_id)
    if request.method == 'POST':
        cliente = request.form['cliente']
        if servico is None:
            # Se o serviço não existe, redireciona para a página inicial
            return redirect(url_for('index'))
    
        if request.method == 'POST':
            novo_agendamento = Agendamento(cliente=cliente, servico_id=servico.id)
            db.session.add(novo_agendamento)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('agendar.html', servico_id=servico_id)

# Outras rotas e configurações...
if __name__ == "__main__":
    app.run(debug=True)