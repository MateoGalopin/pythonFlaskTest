#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
curl -X DELETE http://127.0.0.1:5000/article -H "Content-Type: application/json" -d '{"id": "1"}'
'''

from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)

@app.route('/articleData', methods=['DELETE'])
def delete_item_data():
    id = request.json.get('id')
    print( "id", id, request )
    return jsonify({"result": "OK" }), 200

@app.route('/articleArgs', methods=['DELETE'])
def delete_item_args():
    id = request.args.get('id')
    print( "id", id, request )
    return jsonify({"result": "OK" }), 200

@app.route('/article/<int:id>', methods=['DELETE'])
def delete_item(id):
    print( "id", id, request )
    return jsonify({"result": "OK" }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
