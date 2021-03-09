# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:28 2021

@author: AzertWay
"""
from flask import Flask
from flask_restful import reqparse
from P5_03_final import main

app = Flask(__name__)


@app.route('/data_preprocessing')
def get():
    try:
        data = main('../input/labeled_data1.csv')
    except FileNotFoundError:
        return {
                'message': 'File not found'
            }, 404
    return {'data': data}, 200  # return data and 200 OK


@app.route('/data_preprocessing')
def post():
   pass
 

if __name__ == "__main__":
    app.run()
