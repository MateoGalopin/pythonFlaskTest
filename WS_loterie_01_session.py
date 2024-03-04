#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
pip install waitress

Dans votre api :
from waitress import serve
Dans le 
if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=5000)

waitress-serve --port=5000 nom_api_sans.py:app  
'''

# Première requête pour initialiser la session et sauvegarder le cookie
# curl -c cookies.txt http://localhost:5000/init

# Requêtes suivantes en utilisant le cookie sauvegardé
# curl -b cookies.txt http://localhost:5000/test/50

from flask import Flask, request, jsonify, session
#from flask_session import Session  
# pip install flask-session
from flask_cors import CORS
import random    

app = Flask(__name__)
CORS(app)

app.secret_key = '1234'
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

@app.route('/init', methods=['GET'])
def init():
    nombre_secret = random.randrange( 0, 100 ) 
    session[ 'tirage' ]     = nombre_secret
    session[ 'ip' ]         = request.environ[ 'REMOTE_ADDR' ]
    session[ 'agent' ]      = request.environ[ 'HTTP_USER_AGENT' ]
    print( ">>", nombre_secret )
    return jsonify(  { "result" : 'OK' } ), 200

@app.route('/test/<int:val>', methods=['GET'])
def test(val):
    nombre_secret = session[ 'tirage' ]
    print( ">>", nombre_secret, val     )
    print( "header", dict(request.headers)  )
    print( "cookie", dict(request.cookies)  )
    print( "sesion", dict(session)          )
    print( "enviro", dict(request.environ) )

    if session[ 'ip' ] != request.environ[ 'REMOTE_ADDR' ]:
        print( 'erreur IP')
    if session[ 'agent' ] != request.environ[ 'HTTP_USER_AGENT' ]:
        print( 'erreur IP')
       
    if val > nombre_secret :
        return jsonify({"resultat": "-"}), 200
    if val < nombre_secret :
        return jsonify({"resultat": "+"}), 200
    return jsonify({"resultat": "="}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
