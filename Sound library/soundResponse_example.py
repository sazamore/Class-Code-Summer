#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:18:09 2020

@author: Dr. Z

Demonstration of how to use soundResponse.py as an imported library.
soundResponse.py MUST be in the same folder as your file and
    MUST be submitted with your code!
    
This demonstration uses a soundResponse Ctrlr object to play music based on keystroke. ('s' key will start and stop the music)
You can use this code to:
    1. Understand how to use the soundResponse class. Amplitude (loudness) is shown in this example, but you can do a similar task
    with frequency (pitch) by using music.getCurrFreq()[0]
    2. Understand how to overwrite callback functions so that the same keypress will do 2  things. (See lines 45, 68, and 70)
    
PROTIP: If imported, this borrowed code only counts as 1 line of outside code.

"""

import soundResponse as SR
import turtle

panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0)    
turtle.tracer(0)


circ = turtle.Turtle(shape='circle')
circ.up()
circ.goto(300,300)

music = SR.Ctrlr('tech.wav') # create object
run = True

def stop():
    '''callback function that stops animation while it's running'''
    global run
    run = False
    panel.onkey(go,'s') # change the function of the s key press  back to go


def go():
    '''Callback function that plays sound and does entire animation'''
    global run
    music.start() # start song
    
    while run:
        amp = music.getCurrAmp()[0]/1000 #work only with the first value returned, the amplitude
        circ.shapesize(amp) 
    #    print(amp)
    
        if amp > 3:
            circ.color('lightblue','lightblue') #turn light color if really loud.
        else:
            circ.color('black','black')
    
        turtle.update()
        
        # quit the while loop when the song ends
        if amp ==-1:
            run = False
        panel.onkey(stop,'s') # change the function of the s key press.

panel.onkey(go,'s')  # start off with one function for the s key  press...
turtle.listen() # required for key presses
        
turtle.done()
