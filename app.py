from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Visualizza i voti
    if os.path.exists('voti.txt'):
        with open('voti.txt', 'r') as f:
            contenuto = f.read()
    else:
        contenuto = "Nessun voto ancora inserito."

    if request.method == 'POST':
        # Aggiungi un nuovo voto
        if 'nome_professore' in request.form and 'voto' in request.form:
            nome_professore = request.form['nome_professore']
            voto = request.form['voto']

            with open('voti.txt', 'a') as f:
                f.write(f"{nome_professore}: {voto}\n")

            # Ricarica i voti dopo l'inserimento
            with open('voti.txt', 'r') as f:
                contenuto = f.read()

        # Cancella i voti se è stato premuto il pulsante
        if 'cancella_voti' in request.form:
            try:
                os.remove('voti.txt')
                contenuto = "I voti sono stati cancellati!"
            except FileNotFoundError:
                contenuto = "Non ci sono voti da cancellare."

    return render_template('index.html', voti=contenuto)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)