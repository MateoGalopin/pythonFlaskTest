#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X POST http://localhost:5000/multiply 
-H "Content-Type: application/json" 
-d '{"v1": "3", "v2": "4"}'
'''
from flask import Flask, request, jsonify
from flask_cors import CORS

# La clé secrète pour l'authentification (dans un cas réel, stockez-la de manière plus sécurisée)
API_KEY = "toto123"

app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['POST'])
def multiply():

    # coté back
    # Vérifier la clé d'authentification

    auth_key = request.headers.get('Authorization')
    if auth_key != API_KEY:
        return jsonify({"error": "Clé d'authentification invalide"}), 403

    # Effectuer l'opération d'addition
    data = request.json
    v1 = data.get('v1')
    v2 = data.get('v2')

    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400
    try:
        product = float(v1) * float(v2)
        return jsonify({"result": product}), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

