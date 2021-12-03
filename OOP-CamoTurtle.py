#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 1 22:13:36 2021

@author: sazamore

CamoTurtle

************************************************************
**      YOUTUBE TUTORIAL: https://youtu.be/cNEGXOJ2toY    **
************************************************************

Objective:
    Try to click on any of the target turtles!
Rules:
    Click on the target turtles.
    TODO: before time runs out!
Challenge:
    The target turtles are the same color as the camouflage background.
Interactions:
    User can click on the target turtles, but not the camouflage ones!


This is an example of fully OOP code.
 
Things to note!
    1. The manager class is called turtleGame. It was the last thing I developed.
    2. I call setup in the init method of turtleGame, meaning it will be called
    when a turtleGame instance (an object) is  made.
    3. I needed an attribute to change when the game ended. I used pen down when
    clicked, and then used the turtle method isDown() to check the pen 
    position (lines 78 and 147)
    4. The Mover objects needed to access the panel. I made that a required parameter
    of the Mover class (line 32)
    
"""
import turtle
import random, time

# ================== DEFINE CLASSES =====================
class Movers(turtle.Turtle):
    def __init__(self,panel,x=0,y=0):
        """Gets called when the class instance is made.
        Arguments:
            x - start horizontal location. Defaults to 0
            y - start vertical location. Defaults to 0"""
        super().__init__() # call the parent/super class' init method
        # insures compatability and access to parent/super class
        
        self.panel=panel #requires the screen that all the animation will happen on
        
        
        self.shape('turtle') # set shape to turtle
        self.color('forestgreen') #they're all green
        
        # shape setup
        self.shapesize(2) # make it a little bigger
        self.seth(random.randint(0,360))
        self.up()
        self.goto(x,y) # go to start position
        
        self.onclick(self.gotMe)
        self.panel.update() # Draw the turtle object on the screen
        
    def walk(self):
        """sends the object in a random walk"""
        self.forward(random.randint(3,20))
        self.seth(random.randint(0,360))
        self.panel.update() # draw it to the screen!
        
    def gotMe(self,x,y):
        '''when user clicks on turtle, highlights the clicked
        turtle, prints text to screen and changes the global
        running value to False (for animation control)'''
        self.color("black") # Turn selected turtle Black
        self.panel.update()     # draw on Screen
        
        self.down() # drop pen so we can look for it elsewhere
        
# ================= DEFINE FUNCTIONS ====================
class turtleGame():
    def __init__(self):
        # make panel attributes
        self.panel = turtle.Screen()
        self.w = 600
        self.h = 600

        # animation attributes
        self.running = True 
        # with running as an attribute, any object can check to 
        # see if its value is True or False!
        
        # Text features
        self.font = ("helvetica",40,"bold")
        
        # Instantiate other classes
        self.camo = Movers(self.panel) #single Movers object example (see run method)
        
        # Multiple Movers objects (PROMOVE: this can go into a method!)
        self.targetList = [] # empty list for multiple Movers objects
        self.numTargets = 3
        for i in range(self.numTargets):
            self.targetList.append(Movers(self.panel,random.randint(-200,200),random.randint(-200,200)))
        
        # start the game upon instantiation
        self.setup()
        
    def camoBg(self, text="Click the turtle to win!"):        
        for i in range(400):
            x = random.randint(-self.w/2,self.w/2)
            y = random.randint(-self.h/2,self.h/2)
            self.camo.goto(x,y)
            self.camo.stamp()
        self.panel.update()
        time.sleep(1) #wait before showing instructions and starting game
        
        self.camo.color('black') # change text color to black
        self.camo.goto(-200,-100)
        self.camo.write(text,font=self.font)
        self.panel.update()
        
        # pause then erase instructions
        time.sleep(3)
        self.camo.undo() # the last action was writing
        self.camo.ht()
    
    def gameOverWrite(self,x=-200,y=0):
        '''Uses Movers object (camo) to write game over text'''
        self.camo.up()
        self.camo.goto(x,y) # go below click location
        self.text = "You got me! Game over!"
        
        self.camo.write(self.text,font=self.font)
        self.panel.update() # draw on Screen
    
    def setup(self):
        '''Creates screen, background and start conditions for
        simple click game'''
        turtle.colormode(255) # accept 0-255 RGB values
        turtle.tracer(0) # turn off turtle's animation
    
        self.panel.setup(width=self.w, height=self.h)
        
        #Set background color to dark green
        self.panel.bgcolor('darkgreen')
        
        # create a Mover to randomly stamp all over the screen
        self.camoBg()
        self.run()
    
    def run(self):
        while self.running:
            # EXAMPLE: single Mover object animation
            self.camo.walk() # move the single movers object
            
            # EXAMPLE: each Mover object in a list of Movers objects
            for inst in self.targetList:
                inst.walk()
                if inst.isdown():
                    # check for end condition
                    self.running = False
                    self.gameOverWrite()
            time.sleep(.1) # control frame speed
    

# ================== SETUP & ANIMATION =====================

if __name__=='__main__':
    turtleGame()
    turtle.mainloop() # cleanup and listening for user interactions
        
        
        
