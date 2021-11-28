"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z
@author: YOURNAME HERE

This code slowly changes background from red to yellow and back, continuously
"""
import turtle, random 
turtle.tracer(0)


turtle.colormode(255) # ADD THIS TO YOUR CODE!

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE VARIABLES BELOW=========
panel=turtle.Screen()
running = True # for controlling the while loop
red = 255
green = 255
blue = 0
inc = 1

# this turtle is an example to demonstrate the functions below. You will likely
# have to DELETE OR MODIFY THIS TURTLE to get your game to work properly

# =========DEFINE FUNCTIONS BELOW=========

# MODIFY - delete this comment block
# def replaceFunctionName(x,y):
#     '''This function is callback for a mouse click.'''
#     # add the code that you'd like to perform when clicking HERE
#     # if you want to do something at the location of the click, use the parameters x and y in your
#     # code wherever you need (ex: goto(x,y))
    

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========

# INTERACTION FUNCTIONS BELOW 
# add onclick and onkey commands below. 


# =========ANIMATIONS BELOW=========
# code will execute in order within the loop
while running:
    
    #Commend out this if-elif statement to only change 1 time!
    if green == 255:
        inc *= -1 # change it to negative so it goes back to 0
    elif green ==0:
        inc *= -1
    
    green += inc

        
    panel.bgcolor(red, green, blue)
    
    panel.update()


# =========LISTENERS & CLEANUP =========
panel.mainloop() # keep listeners listening DO NOT DELETE
turtle.done() # cleanup whenever we exit the loop DO NOT DELETE.