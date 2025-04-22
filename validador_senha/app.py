from flask import Flask, render_template, request
from validador import calcular_entropia, senha_forte, verificar_pwned

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = {}
    if request.method == "POST":
        senha = request.form["senha"]
        resultado["entropia"] = calcular_entropia(senha)
        resultado["forte"] = senha_forte(senha)
        resultado["vazamentos"] = verificar_pwned(senha)
        resultado["senha"] = senha
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
