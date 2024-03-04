#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X POST http://localhost:5000/client/changefoto/1234  -H "Content-Type: application/json" -d '{ "foto": "GHDGGDGHDV" }'
'''

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/client/changefoto/<id>', methods=['POST'])
def changefoto( id ):
    foto = request.json.get( 'foto' )



    print( ">>", id, foto )
    return jsonify({"result": 'OK' }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
