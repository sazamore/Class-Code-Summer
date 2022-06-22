#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 09:07:50 2021

@author: sazamore

Sound responsive animation - draw a spirograph with mic input
OOP demonstration - everything will be in classes!
"""

import turtle
import liveSound as ls
import time, math, random

turtle.tracer(0)
turtle.colormode(255)

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)

running = True

class soundSpiro(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.inc = 60
        self.outerRad = 50
        self.innerRad = 10
        self.numIt = int(360/self.inc) # the number of iterations to make a complete circle. 

        self.stream = ls.Stream()
        self.soundDraw()

    def spirograph(self):#,inc=60, outerRad=50, innerRad=10):
        '''Draws a circular spirograph, one circle per call.
        Arguments:
            outerRad = the size of the outer circles 
            innerRad = the size of the inner (negative) circle
            inc = space between patterns. Can be used to determine number of repeats to complete pattern.'''
        # numIt = int(360/inc) # the number of iterations to make a complete circle. 
        self.circle(self.outerRad)
        self.forward(self.innerRad)
        self.right(self.inc)    
        turtle.update()
        
    def soundDraw(self):
        while running:
            chunk = self.stream.sample()

            if max(abs(chunk))>=0.01:
                self.spirograph()
        
        
if __name__ =="__main__":
    soundSpiro()
    
turtle.mainloop()
