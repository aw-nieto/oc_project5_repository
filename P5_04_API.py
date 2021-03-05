# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:14:28 2021

@author: AzertWay
"""
from flask import Flask
from P5_03_final import main

app = Flask(__name__)

@app.route('/')
def get():
    data = main('../input/unlabeled_data.csv')
    data = data.iloc[:2,:].to_dict()       # convert dataframe to dict
    return {'data': data}, 200  # return data and 200 OK

if __name__ == "__main__":
    app.run()
