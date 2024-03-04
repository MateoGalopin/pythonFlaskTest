#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X POST http://localhost:5000/multiply  -H "Content-Type: application/json" -d '{"v1": "3.4", "v2": "4.7"}'
curl -X POST http://localhost:5000/multiply  -H "Content-Type: application/json" -d '{"v1": 3.4, "v2": 4.7}'
'''

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json

    v1 = float(data.get('v1'))
    v2 = float(data.get('v2'))
    #v1 = data.get('v1')
    #v2 = data.get('v2')

    return jsonify({"result": v1 * v2 }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
