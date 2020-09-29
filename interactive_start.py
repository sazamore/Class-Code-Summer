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
# sets the window size up here

# define variables here
panel=turtle.Screen()  # make a window using the setup info


# ========== YOU CODE BELOW HERE ===============





panel.mainloop() #keeps listeners on so we can get interactivity\
turtle.done() # turtle clean up