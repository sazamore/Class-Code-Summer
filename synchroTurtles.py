#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:48:01 2020

@author: Dr. Z
Draw squares in opposite directions at the same time.
"""

from turtle import *

LEFT = Turtle() #turtle draws square to left
RIGHT = Turtle() # draws to right
LEFT.speed(10)
RIGHT.speed(10)

for i in range(2):    
    
    
    for k in range(4):
        # draw squares
        RIGHT.forward(50)
        LEFT.forward(50)
        RIGHT.right(90)
        LEFT.left(90)
    
    LEFT.forward(100)
    RIGHT.forward(100)
        
    