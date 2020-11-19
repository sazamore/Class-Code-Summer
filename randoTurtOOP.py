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
# randTurt = turtle.Turtle(shape='turtle') # make it a turtle, cuz they're cute!
# running = True # set up boolean for our while loop
pace = 25
span = 60

class SoundTurt(turtle.Turtle):
    def __init__(self, color):
        turtle.tracer(0)
        super().__init__() # copy all the methods and attributes of turtle
        self.running = True # for animation
        
        # immediately set up turtle and start movements
        self.setup(color)
        self.runTurt()
        
    # define functions
    def stampSquare(self,x,y):
        '''callback function that draws a filled square wherever the turtle is'''
        self.begin_fill()
        for i in range(4):
            self.forward(100)
            self.right(90)
        self.end_fill()
    
    def setup(self, color): 
        # set up the turtle
        self.color(color)
        self.shape('turtle')
        self.shapesize(2) # make it big so we can see it clearly
        self.up() # don't draw, just move around
        self.speed(10)
        self.onclick(self.stampSquare)
        
    def bounce(self):
        '''bounces the turtle if it is past a boundary.
        turt = Turtle object to be passed in
        if the turtle does bounce, it returns a True, otherwise it returns a False'''
        
        # get coordinates
        x = self.xcor()
        y = self.ycor()
        heading = self.heading() #the angle that it's facing
        
        if x < -w/2: # left side boundary
            AOI = 0 - 2*heading # calculate angle of incidence (AOI)
            self.seth(AOI)
            self.goto(-w/2+1,y)
            # print('left')
            return True
    
        elif x > w/2: # right side boundary
            AOI = 180 - 2*heading
            self.seth(AOI)
            self.goto(w/2-1,y)
            # print('right')
            return True
    
        elif y < -h/2: # top side boundary
            AOI = 270 - 2*heading
            self.goto(x,-h/2+1)
            self.seth(AOI)
            # print('top')
            return True
    
        elif y > h/2: # bottom side boundary
            AOI = 90 - 2*heading
            self.goto(x,h/2-1)
            self.seth(AOI)
            # print('bottom')
            return True
        
        else:
            return False
        
    def move(self):
        self.forward(pace) # go forward a random amount of times
        self.left(random.randint(-span,span)) # turn randomly left or right
        panel.update() # draw the changes onto the screen
        
    def playSound(self):
        pass
    
    def runTurt(self): 
        while self.running:
            
            self.move()
           
            soundCue = self.bounce() # adds boundary interactions
            
            if soundCue:
                pass
                # play sound here
            
            # change colors based on x position (changed to gray to boost visibility)
            if self.xcor() < -100:
                self.pencolor('gray')
            elif self.xcor() < 100:
                self.pencolor('navy')
            else:
                self.pencolor('blue')
            panel.update()
        
if __name__=='__main__':
    turt = SoundTurt('green')
    
    panel.mainloop() #keeps listeners on so we can get interactivity\
    turtle.done() # turtle clean up



