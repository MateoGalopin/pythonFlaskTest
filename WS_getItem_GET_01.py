#!/usr/bin/python3
# -*- coding: utf-8 -*-
# curl "http://127.0.0.1:5000//item?article=brouette&SESSIONID=A67FC2"

from flask import Flask, request, jsonify
from flask_cors import CORS   

    
app = Flask(__name__)
CORS(app)

@app.route('/item', methods=['GET'])
def multiply():
    article = request.args.get('article')
    sessid = request.args.get('SESSIONID')
    print( "\n", article, sessid )
    return jsonify(  { "result" : 'OK' } ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
