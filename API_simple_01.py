#!/usr/bin/python3
# -*- coding: utf-8 -*-

# curl -X GET http://127.0.0.1:5000/
# curl -X POST http://127.0.0.1:5000/
# curl -X PUT http://127.0.0.1:5000/
# curl -X DELETE http://127.0.0.1:5000/

# pip install Flask PyJWT

from flask import Flask, request, jsonify
from flask_cors import CORS   

app = Flask(__name__)

CORS(app)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homeGET():
    print( "appel méthode GET")
    return jsonify({'message': 'Succes'}), 200
    #return jsonify({'message': 'Échec'}), 500

@app.route('/', methods=['POST'])
def homePOST():
    print( "appel méthode POST")
    return jsonify({'message': 'Succes'}), 200
    #return jsonify({'message': 'Échec'}), 500

@app.route('/', methods=['PUT'])
def homePUT():
    print( "appel méthode PUT")
    return jsonify({'message': 'Succes'}), 200
    #return jsonify({'message': 'Échec'}), 500

@app.route('/', methods=['DELETE'])
def homeDELETE():
    print( "appel méthode DELETE")
    return jsonify({'message': 'Succes'}), 200
    #return jsonify({'message': 'Échec'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
