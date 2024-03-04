#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://<adresse_ip>:5000/multiply?v1=3&v2=4"

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

keyClient = 'd11f1378095f9147a4606a7885d56212ad3193e1d38c922357d5404f0522d18b'


@app.route('/multiply', methods=['GET'])
def multiply():
    v1 = request.args.get('v1')
    v2 = request.args.get('v2')
    key = request.args.get('idKey')

    if key is None:
        return jsonify({"error": "non autorisé"}), 401

    if key != keyClient:
        return jsonify({"error": "clé invalide"}), 401

    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400

    try:
        product = float(v1) * float(v2)
        return jsonify(  { "result" : product } ), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
