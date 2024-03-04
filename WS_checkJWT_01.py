#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install Flask PyJWT
# curl -X POST "http://127.0.0.1:5000/multiply?value1=10&value2=5" -H "Content-Type: application/json" -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub20iOiJ0b3RvIiwibnVtZXJvIjoiMTIzMjg2NSIsImV4cCI6MTcwODk3OTM3MH0.KTM0ePAh2PrIaYfl6KxAUxKZ6Xi-2JiYQnFpoJbEOeg" }'

# curl -X GET "http://127.0.0.1:5000/generate_jwt?nom=toto&numero=1232865


from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps
app = Flask(__name__)

# Clé secrète pour la signature JWT (doit correspondre à celle utilisée pour générer le JWT)
SECRET_KEY = "votre_cle_secrete"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.json.get('token')  # Assumer que le token est passé en argument dans l'URL
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            print( jwt.decode(token, SECRET_KEY, algorithms=["HS256"]) )

        except:
            return jsonify({'message': 'Token is invalid or expired!'}), 403
        return f(*args, **kwargs)
    return decorated


@app.route('/generate_jwt', methods=['GET'])
def generate_jwt():
    nom = request.args.get('nom')
    numero = request.args.get('numero')

    if not nom or not numero:
        return jsonify({"error": "Le nom et le numéro de téléphone sont requis"}), 400

    # Création du payload JWT
    payload = {
        'nom': nom,
        'numero': numero,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration après 1 heure
    }

    # Génération du token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return jsonify({"jwt": token})


@app.route('/multiply', methods=['POST'])
@token_required
def multiply():
    try:
        value1 = float(request.args.get('value1'))
        value2 = float(request.args.get('value2'))

    except (TypeError, ValueError):
        return jsonify({'message': 'Invalid input, numbers are required'}), 400

    result = value1 * value2
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)