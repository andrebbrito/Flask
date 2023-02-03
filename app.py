from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/") 
def home():
    return 'Olá esta é minha primeira aplicação Flask'

""" 
Crie uma lista fictícia de usuários. Em cada posição da lista deve 
conter um dicionário com dados (nome, e-mail, idade) de usuários fictícios.
"""

users = [
    {
        "nome": "João da Silva",
        "email": "joao.silva@exemplo.com",
        "idade": 32
    },
    {
        "nome": "Maria José",
        "email": "maria.jose@exemplo.com",
        "idade": 27
    },
    {
        "nome": "Pedro Almeida",
        "email": "pedro.almeida@exemplo.com",
        "idade": 40
    },
    {
        "nome": "Ana Paula",
        "email": "ana.paula@exemplo.com",
        "idade": 35
    }
]

""" 
Crie um endpoint (v1/user/idade/<nome>) que viabilize a consulta de uma idade, 
vinda de um nome que está na sua lista de usuários. Caso não esteja, retorne uma mensagem informando que o usuário não existe.
 """

@app.route('/v1/users/idade/<nome>')
def retorna_idade(nome):
    for user in users:
        if user["nome"] == nome:
            return jsonify({"idade": user["idade"]})

    return jsonify({"mensagem": "Usuário não encontrado"})

""" 
Crie um endpoint (v1/user/email/<nome>) que viabilize a consulta  de um e-mail, vindo de um nome que está na sua lista de usuários. 
Caso contrário, retorne uma mensagem informando que o usuário não existe.
 """
 
@app.route('/v1/users/email/<nome>')
def retorna_email(nome):
    for user in users:
        if user["nome"] == nome:
            return jsonify({"Email": user["email"]})

    return jsonify({"mensagem": "Usuário não encontrado"})


""" 
Crie um endpoint que possibilite uma consulta por nome ou e-mail na lista de usuário e retorne os dados do usuário, contido na lista.
"""

@app.route('/v1/users/<nome>')
def retorna_nomeOrEmail(nome):
    for user in users:
       if (user["nome"] == nome) or  (user["email"] == nome):
            return jsonify({"Nome": user["nome"],"Email": user["email"],"Idade": user["idade"]})       

    return jsonify({"mensagem": "Usuário não encontrado"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)





