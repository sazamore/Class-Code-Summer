"""
Created on Mon Oct  5 13:25:06 2020

@author: Dr. Z

Demonstrates how to select an individual turtle in a list!

You can copy parts of this code and use as is (no changes required, but may be necessary).

"""
import turtle, random 
turtle.colormode(255)

# =========SETUP FOR LISTENERS=========
w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
turtle.listen() # for keyboard listening

# =========DEFINE VARIABLES BELOW=========
panel = turtle.Screen()
running = True # for controlling the while loop
numTurt = 3

colors = ['black','blue','white']

# Create an empty list. We'll add to this list in a for loop, using list functions
turtList = []

# STEP 1. Add turtles to your list using a for loop
for i in range(numTurt):
   turtList.append(turtle.Turtle(shape='circle')) # append adds a turtle to the end of the list.


# =========DEFINE FUNCTIONS BELOW=========

def clickWho(x,y,buffer=30):
    for i in range(len(turtList)):
        turtX = turtList[i].xcor() # get x position of each bubble
        turtY = turtList[i].ycor() # get y position of each bubble
        # breakpoint()
        if turtX - buffer < x < turtX + buffer and turtY - buffer < y < turtY + buffer:
            # see if click is within some range. Default is + or - 10 pixesls
            return i #when a click happens inside of a bubble area, return the index of the turtList

def delTurt(x,y):
    '''Callback function for onclick to delete the selected turtle''' 
    # use the output of the selected 
    selected = clickWho(x,y) 
    
    # use the index to hide and delete the clicked turtle!
    turtList[selected].hideturtle() # we can use variables that will come up later for callbacks ONLY
    turtList.pop(selected) # get rid of the clicked turtle from the list

# =========SET UP TURTLE(S) BELOW (color, size, shape, etc)=========

# STEP 2. Use a for loop to make changes to your turtles. Note how the loop is different from above!
# the function len gets the length of a list!
for i in range(len(turtList)):
    turtList[i].shapesize(4)
    turtList[i].color(colors[i]) # how would this line change if I want each turtle to be a diff color?
    turtList[i].up()
    turtList[i].goto(random.randint(-100,100),random.randint(-200,200))
    
    # we can add our click functions to each TURTLE as we make & modify them!
    turtList[i].onclick(delTurt)

# INTERACTION FUNCTIONS BELOW (onclick)


# =========ANIMATIONS BELOW=========
# while running:

    # STEP 3. Use a for loop to apply the function to each turtle. Note how the loop is different AGAIN!
       

panel.mainloop() 
turtle.done() 