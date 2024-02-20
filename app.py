
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/projeto'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)

# parte do banco de dados
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/cadastra')
def cadastra():

    return render_template('cadastra.html')

@app.route('/perfil')
def perfil():

    return render_template('usuario.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':
        try:
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
        except KeyError as e:
            # Lidar com campos de formulário ausentes
            return "Erro: o campo necessário '{}' está ausente.".format(e.args[0]), 400

        pessoa = Pessoa(
            nome=nome,
            email=email,
            senha=senha
        )

        db.session.add(pessoa)
        db.session.commit()     
        return redirect('/')
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
