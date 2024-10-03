from flask import Flask, request, jsonify
import db

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

app.run(debug =True)
