#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install flask
# pip install flask-cors

# curl "http://localhost:5000/temperature"
# curl "http://localhost:5000/date"


from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/time', methods=['GET'])
def get_current_tim():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.route('/temperature')
def get_temperature():
    return str(random.randrange( -5, 35 ))+'°'


@app.route('/menu')
def get_menu():
    return 'salade de harengs<br>parmentier<br>tarte à la pomme de terre'



@app.route('/listeRandom', methods=['GET'])
def listeRandom():
    nbr_valeurs = int(request.args.get('nombre'))
    datas=[]
    for i in range( nbr_valeurs ):
        datas.append( random.randint( 0, 100 ) )
    
    return jsonify({ 'liste' : datas }), 200

#if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=True)
