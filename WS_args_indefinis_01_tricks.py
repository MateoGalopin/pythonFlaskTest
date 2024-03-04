#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000/route?v=3&nom=toto&age=30"

from flask import Flask, request, jsonify
from flask_cors import CORS
  
app = Flask(__name__)
CORS(app)

@app.route('/<path:params>', methods=['GET'])
def routeslash( params ):

    list_params = params.split( "/" )

    print( ">>", list_params  ) 
    
    return jsonify({'result': "OK" }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
