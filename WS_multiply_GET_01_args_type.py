#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/multiply/3/23/2/5"


from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/multiply/<path:arguments>', methods=['GET'])  
def multiply( arguments ):
    args_list = arguments.split('/')
    result = 1
    for arg in args_list:
        result *= float(arg) 
    
    return jsonify({'result': result }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
