#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:13:50 2020

@author: Dr Z

THIS IS A LIBRARY!

A turtle bounces around the screen 5 times using the same function from
bounceTurt.py

Another turtle draws a line behind it, which turns into a wall. 
isCollision to detect interactions.

HOW TO USE THIS CODE:
    
    1. You can run it! And see how it works!
    2. You can import it, and use the methods inside the library!
        import boundary, turtle
        turt = turtle.Turtle()
        boundary.bounce(turt)
"""


import turtle, random, time


class Boundary:
    global panel, w, h
    def __init__(self):
        self.lead = turtle.Turtle(shape='square')
        self.lead.color('red')
        self.segments=[]
    
    # from bounceTurt.py
    def bounce(self,turt):
        '''bounces the turtle if it is past a boundary.
        turt = Turtle object to be passed in
        if the turtle does bounce, it returns a True, otherwise it returns a False'''
        
        # get coordinates
        x = turt.xcor()
        y = turt.ycor()
        heading = turt.heading() #the angle that it's facing
        
        if x < -w/2: # left side boundary
            AOI = 0 - 2*heading # calculate angle of incidence (AOI)
            turt.seth(AOI)
            turt.goto(-w/2+1,y)
            return True
    
        elif x > w/2: # right side boundary
            AOI = 180 - 2*heading
            turt.seth(AOI)
            turt.goto(w/2-1,y)
            return True
    
        elif y < -h/2: # top side boundary
            AOI = 270 - 2*heading
            turt.goto(x,-h/2+1)
            turt.seth(AOI)
            return True
    
        elif y > h/2: # bottom side boundary
            AOI = 90 - 2*heading
            turt.goto(x,h/2-1)
            turt.seth(AOI)
            return True
        
        else:
            return False
        
    def addSegment(self,color='black', shape='square',width=4):
        self.segments.append(turtle.Turtle(shape=shape))
        self.segments[-1].color(color)
        self.segments[-1].up()
        self.segments[-1].goto(self.lead.pos())
        
    def clear(self):
        self.segments = []
        
    def isCollision(self, turt,target,buffer=30):
        '''Detects collision with an object or list of objects.
        turt is the main object 
        target = the collision target (can be turtle or list of turtles)
        buffer = area surrounding turt center that counts as a collision. Default value is 30 pixels.
        Returns true or false statement if the two items have collided'''
        target = target[:]
        x = turt.xcor()
        y = turt.ycor()
        if type(target)==list:
            # If it's a list, step through each value and check
            if turt in target: #is the turtle we're colliding in the list?
                idx = target.index(turt) # find out where it is
                target.pop(idx) # remove it (just for the function)
            for i in range(len(target)):
                targX = target[i].xcor()
                targY = target[i].ycor()
                if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
                    return True, i # collision detected. Return True *and position in list* and stop running the method.
            return False # no collision detected in list. Return False and stop running the method.
        
        elif type(target)== turtle.Turtle:
            # If it's a turtle, get its position and checks for collision
            targX = target.xcor()
            targY = target.ycor()
            if round(targX)-buffer<=round(x)<=round(targX)+buffer and round(targY)-buffer<=round(y)<=round(targY)+buffer:
                return True
        else:
            return False
        
def run():
    global panel,w,h
    turtle.tracer(0) # animations are turned off
    
    panel = turtle.Screen()
    w = 500
    h = 500
    panel.setup()
    
    running = True
    bounder = Boundary()
    bouncy = turtle.Turtle(shape='circle')
    
    def move(turt):
        if random.randint(0,20)<5:
            turt.left(90)
            turt.forward(10)
        else:
            turt.forward(10)
            
    def gameOver(bounder):
        global running
        hit = bounder.isCollision(bounder.lead,bounder.segments,buffer=5)
        if hit:
            bounder.segments[-1].color('blue')
            for seg in bounder.segments:
                seg.color('red')
                panel.update()
                running=False

            
    bouncy.up()
    bouncy.color('blue')
    bouncy.seth(random.randint(0,360))
    
    count = 0
    while count<5:
        bouncy.forward(10)
        hit = bounder.bounce(bouncy) #ahaha I'm terrible at naming things.
        if hit:
            count += 1
        time.sleep(0.03)
        panel.update()
    
    while running:
        bounder.addSegment()
        move(bounder.lead)
        gameOver(bounder)
        panel.update()

if __name__=='__main__':

    run()
    
            
        
        
        
        
            
            
    
