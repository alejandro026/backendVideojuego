from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps
import json

app = Flask(_name_)
CORS(app)  # Esto habilitará CORS para todas las rutas
app.config["MONGO_URI"] = "mongodb+srv://Johan:Johan@dbloginreact.2ljvu.mongodb.net/AventurasMexicanas"
mongo = PyMongo(app)

@app.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    print(data)
    name = data['nombreJugador']
    score = data['puntos']
    mongo.db.nivel_dos.insert_one({'nombreJugador': name, 'puntos': score})
    return jsonify(message="Score added successfully"), 201

@app.route('/top_scores', methods=['GET'])
def get_top_scores():
    top_scores = list(mongo.db.nivel_dos.find().sort('puntos', -1).limit(5))
    for score in top_scores:
        score['_id'] = str(score['_id'])  # Convertir ObjectId a string
    return jsonify(top_scores), 200


if _name_ == "_main_":
    app.run(debug=True)