# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:16:25 2018

@author: dell
"""
def bl():
    global G
    G = {}


def set_v(key, value):
    G[key] = value


def get_v(key):
    return G[key]
    
    