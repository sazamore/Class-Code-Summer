#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 08:47:39 2021

@author: sazamore

Matching click example code

Uses a Marker object to make buttons on the screen. 
Checks color to see if a match occurs!

Basics: 
    1. You need an attribute or global variable to keep track of whether a button
    was clicked or not. This attribute is in the Marker class.
    2. This attribute or global variable should hold an identifier of the object 
    clicked--I recommend using list index as the identifier for ease.
    3. You'll need a value to compare across clicked objects. Here, it's using color, but it can be
        size, position, shape...anything that's varying among your polymorphic objects!
    4. I recommend a reset method, since there are many outcomes that will reset the value.
"""
import turtle, random

COLORS = ['pink', 'orange','green'] # global palette (legal OOP)

class Marker(turtle.Turtle):
    
    def __init__(self,x=0,y=0):
        super().__init__()

        # track clicks
        self.clicked = False

        # set up Turtle
        self.up()
        self.shape('circle')
        self.shapesize(2)
        self.color(random.choice(COLORS))
        self.goto(x,y)
   
        self.onclick(self.tapped)
        
    def tapped(self,x,y):
        # detect single click, but not double click.
        # if self.clicked:
        #     self.clicked = False
        # else:
        self.clicked = True # save the first color value to the list
        print('click')
        
class Match:
    '''Manager class'''
    def __init__(self):
        self.markerList = []
        self.numMarkers = 4
        self.running = True
        
        # track clicking
        self.clickList = []
        
        # call methods upon instantiation
        self.setup()
        #self.run()
        
    def setup(self):
        '''Create panel and list of markers'''
        panel = turtle.Screen()
        panel.setup()
        
        for i in range(self.numMarkers):
            self.markerList.append(Marker(-200+(i*150))) # space out markers
            
    def resetMarker(self):
        '''Reset values if no match found.'''
        for idx in self.clickList:
             # reset marker status, starting with end of
             self.markerList[idx].clicked = False
        self.clickList = []            
    
    def run(self):
        while self.running:
            # each frame, check for match
            for i in range(len(self.markerList)):
                
                if self.markerList[i].clicked and i not in self.clickList:
                    # only add clicked info if less than 2 clicks
                    # i not in self.clickList makes sure you don't click the same marker 2x
                    
                    # use list index to perform checks
                    self.clickList.append(i) # store list index of clicked object
                    # print(self.clickList) # uncomment for reporting
                    break # stop searching through list!
                    
                # check if enough clicks for match
                if len(self.clickList)==2:
                    if self.markerList[self.clickList[0]].color()[0] == self.markerList[self.clickList[1]].color()[0]: 
                        # colors match
                         for idx in self.clickList:
                             # hide clicked objects
                             self.markerList[idx].ht()
                             self.resetMarker()
                    else:
                        # no match, tell the user!
                        print('WRONG!')
                        
                        # reset marker status
                        self.resetMarker()
                turtle.update()
                        
Match().run()
turtle.mainloop()

        
        