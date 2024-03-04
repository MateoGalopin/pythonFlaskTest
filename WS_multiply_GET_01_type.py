#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/multiply/3.2/4.11"

from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/multiply/<float:v1>/<float:v2>', methods=['GET'])

def multiply( v1, v2 ):
    product = v1 * v2
    return jsonify(  { "result" : product } ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
