#!/usr/bin/python3
# -*- coding: utf-8 -*-


# pip install Flask PyJWT
# curl -X POST http://127.0.0.1:5000/generate_jwt -H "Content-Type: application/json" -d "{\"nom\":\"toto\", \"numero\":\"1234567890\"}"


from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Clé secrète pour la signature JWT (à garder secrète !)
SECRET_KEY = "votre_cle_secrete"

@app.route('/generate_jwt', methods=['POST'])
def generate_jwt():
    data = request.json
    nom = data.get('nom')
    numero = data.get('numero')

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

if __name__ == '__main__':
    app.run(debug=True)
