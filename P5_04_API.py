# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:28 2021

@author: AzertWay
"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
from P5_03_final import classification

app = Flask(__name__)
api = Api(app)


class Classification(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Title', required=True)
        parser.add_argument('Body', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
    
        data = classification(args)
            
        return {'message': data[0]}, data[1]


def get_port():
  return int(os.environ.get("PORT", 5000))


api.add_resource(Classification, '/')

if __name__ == "__main__":
    app.run(debug=False, port=get_port(), host='127.0.0.1')
