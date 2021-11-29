#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:51:57 2021

@author: sazamore

Populate
(Fully OOP)

Shows how to make and move many objects in a visual display.
    See spawn method.  

Use bounce method from the Bouncer class to simulate jumping!
For Jumping, velocities should be positive & if statement should stop jump (set isBounce to False)
Bounce method code modified from:
    http://techforcurious.website/simulation-of-bouncing-ball-vpython-tutorial-visual-python/
v(t+dt) = v(t) + g*dt

"""

import turtle, random

class Manager:
    '''Makes all of the objects and runs the animation'''
    def __init__(self, numCirc=5):
        # set up gameplay
        self.running = True
        self.numCirc = numCirc
        
        # make manyobjects
        self.bounceList = [] #  empty list for items
        self.startBounce() # create bubbles
        
    def spawn(self,numCirc):
        '''Generates list of Bouncer bubbles'''
        for i in range(numCirc):
            self.bounceList.append(Bouncer(random.randint(-300,300)))
        
    def startBounce(self):
        '''Initiates the animation'''
        self.spawn(self.numCirc) # make list
        
        while self.running:
            for bubble in self.bounceList:
                bubble.drop() # call the drop method for each  bubble.
        

class Bouncer(turtle.Turtle):
    '''Blue circular objects that bounce up and down.'''
    def __init__(self, x=0, y=0):
        super().__init__(shape="circle",visible=False)
        
        # setup turtle settings
        self.color('blue')
        self.shapesize(3)
        self.up()
        self.goto(x,y) # startlocation
        self.st()
        turtle.update()
        
        # bubble settings
        self.x = x
        self.y = y
        self.velocity = random.randint(-25,-10) # makes different speed movement
        self.slow = random.randint(3,5) # rate of how quickly energy disipates (low # = many bounces)
        self.g = -9.8    # gravityyyy
        self.dt = 0.1    # increment the timing of your bounce
        self.t = 0       # keep track of the timing of your bounce
        
        # uncomment this line & lines below for jumping
        #self.isJump = False # for use if jumping
                
    def drop(self,bounceSize=20, floor=-300):
        '''Induces gravity and a bounce when it hits lower vertical boundary.
        Arguments:
            floor - lower boundary upon which bouncing starts. Defaults to lower edge of default-sized Screen'''
        # self.isJump = True
        self.velocity = self.velocity + self.g*self.dt
        self.y += self.velocity*self.dt # use speed to update position      
        
        if self.y <= floor:
            self.velocity *= -1 # send it the other direction
            if self.velocity > 0:
                self.velocity -= self.slow # slow it down
            # self.isJump = False
        self.t += self.dt
        self.goto(self.x, self.y)
        
        turtle.update()

#if __name__=='__main__':
Manager()
turtle.mainloop()
        