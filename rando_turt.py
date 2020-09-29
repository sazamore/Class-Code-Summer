#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:51:17 2020

@author: Dr. Z

Creates a turtle that randomly wanders around the screen using a WHILE LOOP.
Has a conditional block that keeps it from going out of bounds.

"""
import turtle, random #didja know you can do this? pretty cool.

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners

# define variables
panel=turtle.Screen()
randTurt = turtle.Turtle(shape='turtle') # make it a turtle, cuz they're cute!
running = True # set up boolean for our while loop
pace = 25
span = 60

# set up the turtle
randTurt.color('green')
randTurt.shapesize(2) # make it big so we can see it clearly
randTurt.up() # don't draw, just move around
randTurt.speed(10)
randTurt.width(3) # made it bigger for visibility


while running:
    
    randTurt.forward(pace) # go forward a random amount of times
    randTurt.left(random.randint(-span,span)) # turn randomly left or right
   
    # define our tests for the while loop
    # use w and h instead of hard coding!
    ybounds = randTurt.ycor()<-h/2 or randTurt.ycor()>h/2
    xbounds = randTurt.xcor()<-w/2 or randTurt.xcor()>w/2
    
    if xbounds or ybounds:
        
        # moves the turtle back to center if it wanders out of bounds
        randTurt.up() # don't draw the path home.
        randTurt.home()

panel.mainloop() #keeps listeners on so we can get interactivity\
turtle.done() # turtle clean up