#!/usr/bin/python3
# -*- coding: utf-8 -*-

# curl  http://localhost:5000/init
# curl http://localhost:5000/test/50

from flask import Flask, request, jsonify
from flask_cors import CORS
import random    

app = Flask(__name__)
CORS(app)

nombre_secret = 0

@app.route('/init', methods=['GET'])
def init():
    global nombre_secret
    nombre_secret = random.randrange( 0, 100 ) 
    print( ">>", nombre_secret )
    return jsonify(  { "result" : 'OK' } ), 200

@app.route('/test/<int:val>', methods=['GET'])
def test(val):
    print( ">>", nombre_secret, val     )
    if val > nombre_secret :
        return jsonify({"resultat": "-"}), 200
    if val < nombre_secret :
        return jsonify({"resultat": "+"}), 200
    return jsonify({"resultat": "="}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
