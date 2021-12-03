#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:53:38 2021

@author: sazamore

Perlin noise example - shows 1D and 2D examples

REQUIRED: INSTALL PERLIN LIBRARY

In Command Line Console, type:
    pip install perlin
Restart kernel

"""
import turtle
import perlin, random, math

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)


# perlin generates noise based on a seed (start point)
# we'll use a random  value so that each iteration of a path is different!

y = perlin.Perlin(random.randint(0,6000)) 
x = perlin.Perlin(random.randint(0,6000)) 
perl = turtle.Turtle()

# 1D path
def perlinTrace(steps=10000):

    for i in range(steps):
        perl.goto(i,x.one(i))
    
# 2D path
def perlin2D(steps=10000):
    for i in range(steps):
        perl.goto(x.one(i),y.one(i))
    
# add perlin noise to shape pattern
# perlin ellipse
def perlinOval(steps=10000):
    for i in range(steps):
        angle = math.radians(i)
        horiz = 200 * math.sin(angle) + x.one(i)
        vert = 30 * math.cos(angle) + y.one(i)
        perl.goto(horiz,vert)
            
#  Call a function to try out different patterns!
        
        