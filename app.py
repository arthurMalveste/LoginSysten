
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/sistema'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)

# parte do banco de dados
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100),unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(11), unique=True)
    preferencia = db.Column(db.String(100), nullable=False)

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
        email = request.form['email']
        senha = request.form['senha']

        pessoa = Pessoa(
            email=email,
            senha=senha
            )

        db.session.add(pessoa)
        db.session.commit()     
        return redirect('/cadastro')
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
