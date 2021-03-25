# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:28 2021

@author: AzertWay
"""
from flask import Flask, jsonify
from flask_restful import Api, reqparse
import os
from P5_03_final import classification

app = Flask(__name__)
api = Api(app)


@app.route('/label/', methods=['POST'])
def post():
    parser = reqparse.RequestParser()  # initialize
    parser.add_argument('Title', required=True)
    parser.add_argument('Body', required=True)
    args = parser.parse_args()  # parse arguments to dictionary

    data = classification(args)

    return jsonify({
        'Message': data[0],
        'METHOD': 'POST'
    }), data[1]

@app.route('/', methods=['GET'])
def index():
    return '<h1>OpenClassrooms - Projet 5 - Catégorisez des questions</h1>'

def get_port():
  return int(os.environ.get("PORT", 5000))


if __name__ == "__main__":
    app.run(debug=False, port=get_port())
