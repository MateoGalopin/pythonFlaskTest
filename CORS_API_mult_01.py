#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install Flask PyJWT
# curl -X GET "http://127.0.0.1:5000/multiply?value1=10&value2=5"

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['GET'])

def multiply():
    try:
        value1 = float(request.args.get('value1'))
        value2 = float(request.args.get('value2'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input, numbers are required'}), 400

    result = value1 * value2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
