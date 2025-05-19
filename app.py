from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome_professore = request.form['nome']
    voto = request.form['voto']
    
    with open('voti.txt', 'a') as f:
        f.write(f"{nome_professore}: {voto}\n")
    
    return "Voto salvato!"

if __name__ == '__main__':
    app.run(debug=True)