#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/somme/2/76/87/9/0"


from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/somme/<path:params>', methods=['GET'])
def routeslash( params ):
    list_param = params.split( '/' )
    somme = 0
    for param in list_param:
        somme += int(param)
    return jsonify({'result': somme }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
