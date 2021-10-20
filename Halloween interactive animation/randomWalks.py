#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:15:23 2021

@author: sazamore

Levy walk with turtles
"""
import turtle
import numpy as np

# Modified from https://towardsdatascience.com/random-walks-with-python-8420981bc4bc
# Define parameters for the walkdims = 2
def levyPath(step_n=1000,scale=50):
    '''makes a 2D path ((x,y)*stem_n) of a levy walks.
    Arguments:
        step_n = Number of steps in path (length of path)
        scale = scaling size of the path, scales steps correspondingly
    Levy walks are characterized by slow progression with infreequent,
    sudden long steps.'''
    step_shape = (step_n,2)
    step_set = [-1, 0, 1]
    scale = 50 
    
    origin = np.zeros((1,2))# Simulate steps in 2Dstep_shape = (step_n,dims)
    steps = np.random.choice(a=step_set, size=step_shape)
    path = np.concatenate([origin, steps]).cumsum(0)
    start = path[:1]
    stop = path[-1:]# Plot the path
    
    path*=scale
    return path

if __name__=='__main__':
    # if you run this as a script, it will execute this code
    # but you can also import this as a library
    
    #plot it
    levy = turtle.Turtle()
    path = levyPath()

    for point in path:
        levy.goto(point[0],point[1])