#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/multiply?v1=3&v2=4&v3=5"


from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/multiply', methods=['GET'])

def multiply():
    result = 1
    for key in request.args:
        result *= float(request.args.get(key)) 
    
    return jsonify({'result': result }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
