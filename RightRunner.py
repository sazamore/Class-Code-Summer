#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:50:23 2021

@author: sazamore

OOP example of arrow movement with key press. Runner object moves to the right
F O R E V E R.
This example does not use animation. The listening method and mainloop keeps the program
continually listening for interactions. The callback functions update the panel.

NOTE:
    1. Key presses require callback functions with NO PARAMETERS (self excluded)
    2. You also need to call turtle.listen() and turtle.mainloop()
"""
import turtle

class Runner(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.tracer(0)
        self.panel = turtle.Screen()
        
        self.up()
        self.shape('triangle')
        self.shapesize(3)
        self.step = 15
    
        # set up callbacks, PANEL ONLY
        self.panel.onkeypress(self.right,"Right")
        # see turtle documentation for keyboard button names and moremore.
        
        # turn on listener REQUIRED
        turtle.listen()
    
    def boundary(self):
        '''Wraparound boundary'''
        w = self.panel.window_width() 
        if self.xcor() > w/2:
            self.goto(-w/2, self.ycor())
        turtle.update()
        
    def right(self):
        '''Continuous rightward movement'''
        self.setheading(0) # face right
        self.forward(self.step)
        self.boundary() # check position
            
            
if __name__ == '__main__':
    Runner()
    turtle.mainloop()