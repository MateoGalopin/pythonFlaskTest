#!/usr/bin/python3
# -*- coding: utf-8 -*-

# linux
# curl -X POST http://localhost:5000/multiply  -H "Content-Type: application/json" -d '{"v1": "3", "v2": "4"}'

# windows
# curl -X POST http://127.0.0.1:5000/multiply -H "Content-Type: application/json" -d "{\"v1\": \"3\", \"v2\":\"4\"}"

from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['POST'])
def multiply( ):

    v1 = request.json.get( 'v1' )
    v2 = request.json.get( 'v2' )
    
    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400

    try:
        product = float(v1) * float(v2)
        return jsonify(  { "result" : product } ), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400

@app.route('/divide', methods=['POST'])
def divide( ):

    v1 = request.json.get( 'v1' )
    v2 = request.json.get( 'v2' )
    
    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400

    try:
        product = float(v1) / float(v2)
        return jsonify(  { "result" : product } ), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
