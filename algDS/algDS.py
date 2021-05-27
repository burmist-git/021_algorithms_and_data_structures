#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date        : Wed May 26 23:11:03 CEST 2021
Autor       : Leonid Burmistrov
Description : Data Structures and Algorithms
"""

import pandas
import json
import os.path
import time

def get_config_json(filename="./ect/config.json"):
    """
    Example to read json config file    
    """
    return json.load(open(filename))

def print_config(config):
    """
    Print config
    """
    print(type(config))
    print(config.keys())
    print(config["par1"])
    print(config["par2"])
    print(config["par3"])

def printinfo(func):
    def wrapper(**aw):
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func(**aw)
    return wrapper

@printinfo
def shan_ex_01_01_01(a,b):
    print("a = ",a)
    print("b = ",b)
    t = a
    a = b
    b = t
    print("a = ",a)
    print("b = ",b)

@printinfo
def shan_ex_01_01_02(a,b):
    print("a = ",a)
    print("b = ",b)
    a = a + b
    b = a - b
    a = a - b
    print("a = ",a)
    print("b = ",b)

    
    
def main(filename="./ect/config.json"):
    """
    Definition of the main function (use for testing only)
    """
    config=get_config_json(filename=filename)
    print_config(config)
    shan_ex_01_01_01(a=3,b=6)
    shan_ex_01_01_02(a=3,b=7)
    
if __name__ == "__main__":
    main()
