#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X POST http://localhost:5000/multiply/2.3 -H "Content-Type: application/json" -d '{"v1": 3.4 }'
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/multiply/<float:v2>', methods=['POST', 'GET'])
def multiply( v2 ):
    v1 = float(request.json.get('v1'))
    return jsonify({"result": v1 * v2 }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
