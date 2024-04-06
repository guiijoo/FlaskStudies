from flask import Flask, url_for, render_template


#incialização
app = Flask(__name__)

#rotas
@app.route("/")
def main():
    titulo = "Setor de T.I."
    usuarios = [
        {"nome" : "guiijoo", "membro_ativo" : True},
        {"nome" : "Julio magago", "membro_ativo" : False},
        {"nome" : "Carlos Gommes Tavares", "membro_ativo" : False},
        {"nome" : "Edson Nassuato", "membro_ativo" : True}
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

#execução
app.run(debug=True)