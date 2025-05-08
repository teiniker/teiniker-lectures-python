from flask import Flask, render_template, request
from translator import TranslatorServiceGerman, TranslatorServiceFrench

app = Flask(__name__)

# http://localhost:8080/
@app.route('/')
def index():
    return render_template('index.html')

# http://localhost:8080/translator
@app.route('/translator', methods=['POST'])
def translate():
    language = request.form.get('language')
    word = request.form.get('word')

    if language == "Deutsch":
        service = TranslatorServiceGerman()
    else:
        service = TranslatorServiceFrench()

    translation = service.translate(word)

    return render_template('translation.html', word=word, translation=translation)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
