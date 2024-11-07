from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["*"]}})  

# Configuração do MongoDB
client = MongoClient('mongodb+srv://recinproj:NRdhqU14UA14vJF5@cluster0.r8fkm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['inova-gastro'] 
agendamentos_collection = db.leads


@app.route('/resgatar', methods=['POST'])
@cross_origin()
def resgatar():
    data = request.json
    email = data.get('email')
    nome = data.get('nome')
    mensagem = data.get('mensagem')
    
    # Verificar se o email já existe no banco de dados
    usuario = agendamentos_collection.find_one({"email": email})
    
    
    agendamentos_collection.insert_one({"email": email, "nome": nome,  "mensagem": mensagem})
    return jsonify({"status": "sucesso", "mensagem": "Usuário cadastrado com sucesso!"})


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)