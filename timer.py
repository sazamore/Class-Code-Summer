#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:47:44 2020

@author: Dr. Z

Count down timer library

"Deletes" a bar across the screen, with numbers that decrease
"""

import turtle, time


class Timer(turtle.Turtle):
    def __init__(self):
        super().__init__() # copy the turtle object
        self.shape('square')
        self.shapesize=[3,1]
        self.step=1
        self.time=60
        self.bar = 'red'
        self.timenow = 0
        self.timeLeft = 0 # start counter
        
    def drawTimer(self,x,y,time=60,step=1,color='red'):
        '''creates a horizontal bar across top of screen, that ticks down
        toward zero.
        Arguments:
            x - horizontal position of LEFT side of timer bar
            y - vertical position of timer bar
            time - how long the timer runs (seconds)
            step - increment of the time'''
        self.time = time
        self.step = step
        self.bar=color
        self.timeLeft=int(self.time/self.step)
        self.timeNow = self.timeLeft
        self.text = turtle.Turtle(visible=False)
        
        self.up()
        self.goto(x,y)
        self.color(color)
        self.stamp()
        for i in range(self.timeLeft):
            self.forward(self.shapesize[0]) # move forward the size of the 
            self.stamp()
            
    def tick(self,color='white'):
        time.sleep(self.step)
        if self.timenow==0:
            if self.color()[0] == self.bar:
                self.color(color)
                print(self.color)
                self.stamp()
                panel.update()
            else:
                self.backward(self.shapesize[0])
                self.stamp()
                self.timeNow -= self.step
                panel.update()
        
    def showTime(self,x,y):
         self.text.clear()
         self.text.color('black')
         self.text.up()
         self.text.goto(x,y)
         self.text.write(self.timeNow, font=('arial',24))
         print('tick')
         panel.update()
    
if __name__ == "__main__":   
    
    
    panel = turtle.Screen()
    w=400
    h=400
    panel.setup(w,h)
    
    # let's change this around so it'll work with any size:
    # w = panel.window_width
    # h = panel.window_height()
    timer = Timer()
    timer.drawTimer(-w/2+w*.1,h/2-h*.1) # scale to window size
    
    while True:
      timer.showTime(w/2-w*.2,-h/2+h*.1)
      timer.tick()
    
    turtle.done()