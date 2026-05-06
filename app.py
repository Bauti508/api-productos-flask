from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

usuarios_lista = ["Ana", "Juan"]

@app.route("/usuarios")
def usuarios():
    return jsonify(usuarios_lista)

if __name__ == "__main__":
    app.run(debug=True)