#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl http://localhost:5000/generateToken?nom=toto&tel=012315
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/generateToken', methods=['GET'])
def generateToken():
    #data = request.json
    #nom = data.get('nom')
    #telephone = data.get('tel')

    nom = request.args.get('nom')
    telephone = request.args.get('tel')

    token = {   'header' : {  'algo' : 'sha256', 'type':'jwt' }, 
                'payload' : { 'nom' : nom, 'tel' : telephone, 'delay' : 3600 }
            }
    tokenStr = jsonify( token )

    m = hashlib.sha256()
    m.update( str( tokenStr ).encode('utf-8'))
    m.update( b'toto va a la mer' )
    hashToken = m.hexdigest()
    token[ 'sign' ] = { 'hash' : hashToken }

    tokenStr = jsonify( token )
    return tokenStr, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
