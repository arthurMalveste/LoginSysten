from flask import Flask, jsonify, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5e5i_123@localhost/projeto'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)

# Parte do banco de dados
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    msg_cadastro = ""
    return render_template('index.html', msg_cadastro=msg_cadastro)

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
            confirm_senha = request.form['confirm_senha']
        except KeyError as e:
            # Lidar com campos de formulário ausentes
            return "Erro: o campo necessário '{}' está ausente.".format(e.args[0]), 400
        
        if senha == confirm_senha:
            pessoa = Pessoa(
                nome=nome,
                email=email,
                senha=senha
            )
           
            db.session.add(pessoa)
            db.session.commit()     
        else:
            msg_cadastro = "As senhas não coincidem!"

        return redirect('/')
    
    return render_template('cadastro.html', msg_cadastro=msg_cadastro, confirm_senha=confirm_senha)

# Manipulador de erro para página não encontrada (Erro 404)
@app.errorhandler(404)
def pagina_nao_encontrada_erro(error):
    return render_template('404.html'), 404

# Manipulador de erro para erro interno do servidor (Erro 500)
@app.errorhandler(500)
def erro_interno_erro(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
