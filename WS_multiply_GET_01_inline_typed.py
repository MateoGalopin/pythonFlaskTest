#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/multiply/3.5/4.1"

from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)

CORS(app)

'''
@app.route('/multiply', methods=['GET'])
def multiply( ):
    v1  = request.args.get( 'v1' )
    v2  = request.args.get( 'v2' )
'''

# la route est typée
@app.route('/multiply/<float:v1>/<float:v2>', methods=['GET'])
def multiply( v1, v2 ):

    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400

    try:
        product = v1 * v2
        return jsonify(  { "result" : product } ), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400


@app.route('/divide/<v1>/<v2>', methods=['GET'])
def divide( v1, v2 ):

    if v1 is None or v2 is None:
        return jsonify({"error": "Please provide both v1 and v2"}), 400

    try:
        product = float(v1) / float(v2)
        return jsonify(  { "result" : product } ), 200
    except ValueError:
        return jsonify({"error": "v1 and v2 must be numbers"}), 400
    except ZeroDivisionError:
        return jsonify({"error": "divide by zero"}), 400
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
