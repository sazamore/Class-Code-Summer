#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:50:47 2021

@author: sazamore

Demonstrates how to incoporate sound with a mouse interactions
Requires the playsound library, and tech.wav

                                  ---

IF YOU GET AN ERROR ABOU THE PLAYSOUND LIBRARY

In your command line, type in:
    pip install playsound
    pip install PyObjC
    
This will download and install the necessary libaries onto your computer, so that
Python can easily find it. Once installed, run this code again.

                                  ---

SOUNDFILE MUST BE IN THE SAME FOLDER AS SCRIPT.
"""
import turtle
from playsound import playsound
# Sound file must be in the same folder as this (and your) script!

# setup library & panel settings
turtle.colormode(255)
turtle.setup() # turn on listeners (this is already in your start code)
turtle.bgcolor((53, 135, 164)) # blue munsell

# define variables & setup

# Make sure sound file is in the same folde as this script.
sound = 'tech.wav' # replace with the name of your sound file

# Draw the button & some text with turtles
button = turtle.Turtle(shape='square')
text = turtle.Turtle(visible=False)

button.up()
button.shapesize(5)
button.width(3) # thick border on the square
button.color((193, 223, 240),(136, 204, 241)) #columbia blue fill, light cornflower blue outline

text.up()
text.goto(0, 100)
text.write('Click the square \n to play a tune!',font=("Helvetica",18),align="center")

# define functions

def play(x,y):
    '''Plays sound upon clicking (for use with onclick functions)'''
    playsound(sound) # plays the sound
    turtle.bgcolor(45, 137, 139) # change the background color to dark cyan
    
# No animation, so there's no while loop...

# add click interaction for the button only
button.onclick(play)

# cleanup, listeners

turtle.mainloop() # keep listeners on (this is already in your start code)
