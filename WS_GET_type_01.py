#!/usr/bin/python3
# -*- coding: utf-8 -*-

# pip install Flask PyJWT
# curl -X GET "http://127.0.0.1:5000/multiply/10/toto"

#   uwsgi --http 127.0.0.1:5000 --module nom_fic_module:app --processes 4 --threads 2

#   ex :
#   uwsgi --http 127.0.0.1:5000 --module WS_GET_type_01:app --processes 4 --threads 2

from flask import Flask, jsonify

app = Flask(__name__)

# route typée
@app.route('/multiply/<int:nbr>/<string:motif>', methods=['GET'])

# arguement transmis à la fonction
def multiply( nbr, motif ):
    result = nbr * motif
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
