#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, session, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '1234'

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


def htmlspecialchars(text):
    return (
        text.replace("&", "&amp;").
        replace('"', "&quot;").
        replace("<", "&lt;").
        replace(">", "&gt;")
    )

humeurs = []

@app.route('/', methods=['GET'])
def init():
    #if 'humeurs' not in session :
    #    humeurs = []
    #    session[ 'humeurs' ] = humeurs
    return render_template('page.html'), 200

@app.route('/add_humeur/<string:pseudo>/<string:humeur>', methods=['GET'])
def add_ingredient( pseudo, humeur ):
    global humeurs
    print( '>>>', htmlspecialchars(pseudo), htmlspecialchars(humeur) )

    humeurs.append( { 'pseudo' : htmlspecialchars(pseudo), 'humeur': htmlspecialchars(humeur) } )

    #session[ 'humeurs' ].append( { 'pseudo' : pseudo, 'humeur': humeur })
    #session.modified = True 
    return jsonify( {'resultat' : 'OK' } ), 200

@app.route('/list_humeur', methods=['GET'])
def list_ingredient( ):
    #humeurs = session[ 'humeurs' ]
    return jsonify( {'humeurs' : humeurs } ), 200

@app.route('/raz', methods=['GET'])
def raz( ):
    global humeurs  
    humeurs = []
    #session[ 'humeurs' ] = humeurs
    #session.modified = True 
    return jsonify( {'resultat' : 'OK' } ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
