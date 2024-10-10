from flask import Flask, request, jsonify
import db
import exCorrigido as bc


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def hello():
    return "ola mundo"
@app.route('/carro', methods = ["GET"])
def all_cars():

    return jsonify(db.carros, 200)

@app.route('/carro/<int:id>', methods = ["GET"])
def get_cars(id):
    for car in db.carros:
        if car['id'] == id:

            return jsonify (car), 200

    return {'msg': 'Carro nao encontrado', 'status': 404}, 404

@app.route('/carro/oracle', methods = ['POST'])
def insere_carro_oracle():
    carro = request.json
    try:
        bc.insere(carro)
        return carro, 201
    except Exception as e:
        return{'title':'nao foi possivel inserir o carro no banco', 'status':500}, 500
app.run(debug =True)
