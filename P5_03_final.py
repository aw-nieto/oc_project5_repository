# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:21:42 2021

@author: AzertWay
"""
import pandas as pd

def data_import(path):
    return pd.read_csv(path)

def main(*args):
    return data_import(*args)
