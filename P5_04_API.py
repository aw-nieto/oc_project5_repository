# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:28 2021

@author: AzertWay
"""
from flask import Flask
from flask_restful import Resource, Api, reqparse
from P5_03_final import classification, append_data, delete_data

app = Flask(__name__)
api = Api(app)


class Classification(Resource):
    def get(self):
        # get the file path for the file containing the data
        parser = reqparse.RequestParser()
        parser.add_argument('file_path', required=True)
        args = parser.parse_args()
        
        # if no path is given, raises a 400 BAD REQUEST
        if args['file_path'] == '':
            return {"message": {
                "file_path": "File path missing"}}, 400
        
        try:
            data = classification(args['file_path'])
        except FileNotFoundError:
            # if the file is not found, 404 NOT FOUND
            return {'message': 'File not found'}, 404
        
        return {'data': data}, 200  # return data and 200 OK

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('file_path', required=True)
        parser.add_argument('Id', required=True)  # add args
        parser.add_argument('Title', required=True)
        parser.add_argument('Body', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        if args['file_path'] == '':
            return {"message": {
                "file_path": "File path missing"}}, 400

        try:
            data = append_data(args)
        except FileNotFoundError:
            # if the file is not found, 404 NOT FOUND
            return {'message': 'File not found'}, 404
        except ValueError:
            return {'message': 'Id not valid'}, 400
        
        return {'message': data[0]}, data[1]
    
    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('file_path', required=True)
        parser.add_argument('Id', required=True)  # add Id arg
        args = parser.parse_args()  # parse arguments to dictionary
        
        if args['file_path'] == '':
            return {"message": {
                "file_path": "File path missing"}}, 400
        
        try:
            data = delete_data(args)
        except FileNotFoundError:
            # if the file is not found, 404 NOT FOUND
            return {'message': 'File not found'}, 404
        except ValueError:
            return {'message': 'Id not valid'}, 400
        
        return {'message': data[0]}, data[1]

api.add_resource(Classification, '/classification')

if __name__ == "__main__":
    app.run()
