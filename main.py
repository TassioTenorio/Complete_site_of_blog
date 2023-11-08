from flask import  Flask, render_template
# O render serve para importar os files html da pasta templates.

app = Flask(__name__)

lista_usuarios = ['tassio', 'nayara', 'thais', 'maria eduarda']

@app.route("/")   # quando deixamos a rota assim (/) ele entende que é a nossa home page
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)  # O debug é para o site atualizar no momento em que eufizer a atualização.


