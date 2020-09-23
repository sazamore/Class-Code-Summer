#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:48:01 2020

@author: Dr. Z
Draw squares in opposite directions at the same time.
"""

from turtle import *

#  **** add this to use 0-255 values for color! ****
colormode(255) 

gradient = Turtle()
gradient.width(6)

# set color channel variables
red = 238
green = 46
blue = 49

# pick up pen and move to the left edge of the screen
gradient.up()
gradient.goto(-300,0)
gradient.color(red, green, blue) #set the color to our start color
gradient.down()    

for i in range(40):
    #loop to move the turtle forward and change its color
    gradient.forward(15)
    
    # update the color values using ASSIGNMENT OPERATORS
    red -= 3
    blue -=3
    green -=3
    
    # use if statements to limit the color!
    if red < 0:
        red = 0
    if blue < 0:
        blue = 0
    if green < 0:
        green = 0
    
    # change the turtle color
    gradient.color(red, green, blue)
    
done() # clean up so we can close the window after the code runs
        