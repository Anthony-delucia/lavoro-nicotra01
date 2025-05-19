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

@app.route('/visualizza_voti')
def visualizza_voti():
    if os.path.exists('voti.txt'):
        with open('voti.txt', 'r') as f:
            contenuto = f.read()
    else:
        contenuto = "Nessun voto ancora inserito."
    
    return render_template('voti.html', voti=contenuto)

@app.route('/cancella_voti', methods=['POST'])
def cancella_voti():
    try:
        os.remove('voti.txt')
        return "I voti sono stati cancellati!"
    except FileNotFoundError:
        return "Non ci sono voti da cancellare (il file non esiste)."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)