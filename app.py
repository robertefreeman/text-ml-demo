from flask import Flask, render_template, url_for, jsonify, request
import translate # use locally built method

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# create route for domain root
@app.route('/')
def index():
    return render_template('index.html')

# Route for translate API
@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)
