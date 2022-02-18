from flask import Flask, render_template, jsonify

app: Flask = Flask(__name__)

@app.get('/')
def home():
    dicionario = {
        'nome': 'Reperquilson',
        'sobrenome': 'Bastos Nunes',
        }
    return jsonify(dicionario)


@app.get('/digaolah/<n>')
def olah(n):
    return render_template('index.html', nome=n)

@app.post('/form')
def form():
    return 'Funcionou'
