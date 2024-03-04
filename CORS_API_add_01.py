#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install Flask PyJWT
# curl -X GET "http://127.0.0.1:5000/multiply?value1=10&value2=5&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub20iOiJ0b3RvIiwibnVtZXJvIjoiMTIzNDU2Nzg5MCIsImV4cCI6MTcwNjc0MDk5M30.jpYF97Z2ktwlmm2KbdSHM9DC8SvIUnILr6KzLQwmaBQ

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['GET'])
def add():
    try:
        value1 = float(request.args.get('value1'))
        value2 = float(request.args.get('value2'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input, numbers are required'}), 400

    result = value1 + value2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


 