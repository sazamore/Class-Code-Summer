#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:14:34 2021

@author: sazamore

SCARY TIMEZ
A creepy smile moves in a jerky fashion. Giggles and gets in 
your face when you click on the screen.

Requires playsound, randomWalks libraries
"""

import turtle
import time, playsound
import randomWalks as rw

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)

# set up turtle images
panel.bgcolor("black")

#import images and sounds and set it to a turtle
faceS = 'creepy_faceS.gif'
faceLG = 'creepy_faceL.gif'
panel.addshape(faceS)
panel.addshape(faceLG)

# what soundfile will you play?
track = 'imp-laugh.wav' # must be in the same folder as this script

# ================ VARIABLE DEFINITION & SETUP =========================
running = True # 

smile = turtle.Turtle(shape=faceS) # creepy face
smile.up()

# build the smile path
i=0 # increment through path values
path = rw.levyPath(scale=5)

for point in path:
    #keep in boundaries
    if point[0] >= w/2:
        #right
        point[0] = w/2-30
    elif point[0] <= -w/2:
        #left
        point[0] = -w/2+30
    if point[1] >= h/2:
        #bottom
        point[1] = h/2 - 30
    elif point[1] <= -h/2:
        #top
        point[1] = -h/2+30        
        
# ================ FUNCTION DEFINITION =========================

def giggle(x,y):
    '''Makes the face bigger and plays an impish giggle.
    Use with onclick() or onscreenclick() callback functions.'''
    smile.shape(faceLG)
    panel.update()
    playsound.playsound(track)
    smile.shape(faceS)

# ================ ANIMATION LOOP =========================
panel.onclick(giggle)

while running:
    # angle=path(smile,angle)
    smile.goto(path[i%len(path)]) # loop through the list, no matter how long this runs
    i += 1 #increment this value iteratively
    
    panel.update() # update the window with everything drawn in a single frame
    time.sleep(0.01)
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup
