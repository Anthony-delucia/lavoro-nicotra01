from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aggiungi_voto', methods=['POST'])
def aggiungi_voto():
    nome_professore = request.form['nome_professore']
    voto = request.form['voto']

    with open('voti.txt', 'a') as f:
        f.write(f"{nome_professore}: {voto}\n")

    return "Voto aggiunto con successo!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa la porta che Render fornisce
    app.run(host='0.0.0.0', port=port)