from flask import Flask, render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/save_typed_text', methods=['POST'])
def save_typed_text():
    data = request.json
    typed_text = data.get('typedText')

    # Faites ce que vous voulez avec le texte tapé (par exemple, l'enregistrer dans un fichier)
    with open('typed_text_file.txt', 'a') as file:
        file.write(f'Texte tapé : {typed_text}\n')

    return 'Texte tapé reçu et enregistré avec succès'
    
   

if __name__ == '__main__':
    app.run(debug=True)
