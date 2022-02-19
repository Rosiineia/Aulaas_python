from flask import Flask, jsonify, abort, request, make_response
from extensions import db
from models.ngo import  NGO, NGOEncoder

app = Flask('_name_')
app.config['DEBUG'] = True
app.json_encoder = NGOEncoder
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'status': 404, 'error': 'Resource not found'}), 404)





@app.route('/')
def index():
    return '<h1> Encontre uma ONG</h1><p>Este Site é prototipo de uma API para encontrar ONGS</p>'

@app.route('/api/v1/resources/ngos', methods =['GET'])
def  list():
    return jsonify({'ngos':db})

@app.route('/api/v1/resources/ngos/<int:id>', methods =['GET'])
def get(id):
    for ngo in db:
        if id == ngo.id:
            return jsonify(ngo)
    abort(404)

@app.route('/api/v1/resources/ngos', methods=['POST'])
def create():
    if not request.json or not 'name' in request.json:
        abort(400)
    ngo = NGO(request.json['name'],request.json['founder'],
              request.json['sector'])
    db.append(ngo)
    return jsonify(ngo), 201

@app.route('/api/v1/resources/ngos/<int:id>', methods =['PUT'])
def update(id):
    if not request.json:
        abort(400)
    for ngo in db:
        if ngo.id == id:#aqui eu digo o que quero atualizar
            ngo.name = request.json['name']
            ngo.founder = request.json['founder']
            ngo.sector = request.json['sector']
            return jsonify({'done':True})
    abort(404)

@app.route('/api/v1/resources/ngos/<int:id>', methods =['DELETE'])
def delete(id):
    for ngo in db:
        if ngo.id == id:
            db.remove(ngo)
            return jsonify({'done': True})
    abort(404)


app.run()

#ROTA DE ACESSO A API

#OPERAÇÕES
#GET -> CONSULTAS
#POST -> CRIAÇÃO DE RECURSO
#PUT -> ATUALIZAÇÃO DE RECURSO
#DELETE -> EXCLUSÃO