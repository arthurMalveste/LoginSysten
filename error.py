from flask import Flask, render_template

app = Flask(__name__)

# Rota que resultará em um erro 404
@app.route('/pagina-nao-encontrada')
def pagina_nao_encontrada():
    return render_template('404.html'), 404

# Tratamento de erro personalizado para erro 404
@app.errorhandler(404)
def pagina_nao_encontrada_erro(error):
    return render_template('404.html'), 404

# Rota que resultará em um erro 500
@app.route('/erro-interno')
def erro_interno():
    raise Exception("Este é um erro interno do servidor")

# Tratamento de erro personalizado para erro 500
@app.errorhandler(500)
def erro_interno_erro(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False)
