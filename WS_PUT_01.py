#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X PUT http://127.0.0.1:5000/article -H "Content-Type: application/json" -d '{"id": "1", "prix" : 15 }'
'''

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/articleData', methods=['PUT'])
def put_item_data():
    id = request.json.get('id')
    prix = request.json.get('prix')
    print( "id", id, prix )
    return jsonify({"result": "OK" }), 200

@app.route('/articleArgs', methods=['PUT'])
def put_item_args():
    id = request.args.get('id')
    prix = request.args.get('prix')
    print( "id", id, prix )
    return jsonify({"result": "OK" }), 200

@app.route('/article/<int:id>/<float:prix>', methods=['PUT'])
def put_item( id, prix ):
    print( "id", id, prix )
    return jsonify({"result": "OK" }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
