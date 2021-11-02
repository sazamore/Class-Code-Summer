#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:44:57 2021

@author: sazamore

CONTINUOUS CONTOUR SKETCHPAD 
Continuous contour drawing is characterized by artists drawing
without picking up their utensil. Typically the artist stares intently
at the subject, not the drawing surface.

HOW TO USE:
Click and drag to draw with turtle.

THIS IS ALSO:
Example of on drag without retracing glitch.
Code modified from https://stackoverflow.com/questions/19867476/python-turtle-ondrag-not-working
"""
import turtle
turtle.tracer(0)

panel = turtle.Screen()
panel.setup() # turn on listeners
panel.title("Continuous contour sketchpad")
panel.bgcolor('linen')

pen = turtle.Turtle() # this will act as our drawing tool
pen.shapesize(2)  # make it larger so it's easier to drag
panel.update()

# COPY IF LOOKING FOR DRAGGING SOLUTION
def followDrag(x, y):
    '''function for onclick callbacks. You must disable the
    handler and set this function (recursively) to the ondrag
    method to properly drag a turtle.
    From class example repo.'''
    pen.ondrag(None)  # disable handler inside handler

    pen.setheading(pen.towards(x, y))  # turn toward cursor
    pen.goto(x, y)  # move toward cursor
    panel.update()
    
    pen.ondrag(followDrag)
    

#draw only when clicking and dragging
pen.ondrag(followDrag)  # COPY IF LOOKING FOR DRAGGING SOLUTION

turtle.mainloop()  # keep listeners on
