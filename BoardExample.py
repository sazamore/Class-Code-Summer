#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:35:44 2020

@author: master
"""

import turtle, random
turtle.colormode(255)
turtle.tracer(0)

# ===========PANEL/LISTNERS SETUP===============
panel=turtle.Screen()
w=900
h=900
turtle.setup(w,h)

bgcolor = 'gray10'
panel.bgcolor(bgcolor)


class BOARD:
    def __init__(self):        
        
        # board drawing variables
        self.nSquare = 3 # how many tiles on each side do we want in the game?   
        self.color = 'lightsalmon1'

        self.board = turtle.Turtle(shape='circle', visible=False)
        self.interval = w/self.nSquare
        
        # Let's change features of the turtle, self.board, here. 
# =============================================================================
#         #How do we access an attribute after it's made?
# =============================================================================

        # self.draw() # draw the board automatically when we create an object
        
        
    #now let's create a method to draw our board...
    def draw(self):
        '''Draws a tic tac toe board, based on screen size and number of squares!.'''
        hStep = h/(self.nSquare)
        start = -w/2+w/self.nSquare
        
        # draw vertical lines
        for i in range(self.nSquare-1):
            x = start+(i*hStep)
            y = h/2
            
            self.board.up()
            self.board.goto(x,y) # start at the bottom
            self.board.down()
            self.board.goto(x,-y) # go to the top
            
# This class is exactly like BOARD
class BgBOARD(BOARD):
    pass

