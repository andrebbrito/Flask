from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/v1/users/idade/<nome>')
def retorna_idade(nome):
    for user in users:
        if user["nome"] == nome:
            return jsonify({"idade": user["idade"]})

    return jsonify({"mensagem": "Usuário não encontrado"})

if __name__ == '__main__':
    app.run(port=5001, debug=False)



