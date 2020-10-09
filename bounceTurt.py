
  
'''
Bounce Example
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
June 11, 2020
Animated turtle bounces around the screen. Uses a bounce function to detect edtes.
'''

import random, turtle
turtle.colormode(255)
turtle.delay(3000) #waits 3 s before starting

#Create a panel to draw on. 
panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

turt = turtle.Turtle()
running = True


# VariableS!
blues = [(3, 4, 94),(76,175,206),(0, 119, 182),(219,249,244)]
reds = [(100, 18, 32),(133, 24, 42),(167, 30, 52),(189, 31, 54),(224, 30, 55)]
yellows = [(255, 247, 94),(255, 233, 78),(255, 218, 61),(254, 207, 62),(252, 243, 0)]
greens = [(20, 54, 1),(36, 85, 1),(115, 169, 66)]

travel = 0 # initializing counter travel
step = 5 # size of movement increment per "frame"

# function definitions

def bounce(turt):
    '''bounces the turtle if it is past a boundary.
    turt = Turtle object to be passed in
    if the turtle does bounce, it returns a True, otherwise it returns a False'''
    
    # get coordinates
    x = turt.xcor()
    y = turt.ycor()
    heading = turt.heading() #the angle that it's facing
    
    if x < -w/2: # left side boundary
        AOI = 0 - 2*heading # calculate angle of incidence (AOI)
        turt.seth(AOI)
        turt.goto(-w/2+1,y)
        print('left')
        return True

    elif x > w/2: # right side boundary
        AOI = 180 - 2*heading
        turt.seth(AOI)
        turt.goto(w/2-1,y)
        print('right')
        return True

    elif y < -h/2: # top side boundary
        AOI = 270 - 2*heading
        turt.goto(x,-h/2+1)
        turt.seth(AOI)
        print('top')
        return True

    elif y > h/2: # bottom side boundary
        AOI = 90 - 2*heading
        turt.goto(x,h/2-1)
        turt.seth(AOI)
        print('bottom')
        return True
    
    else:
        return False

#Initializations!

# pick up pen and set speed to fastest ()
turt.up()
turt.speed(10)

# send the turtle to a random place
turt.goto(random.randint(-200,200),random.randint(-100,100))
turt.seth(random.randint(0,360))

count = 0
        
while running:
    turt.forward(step)
    
    didBounce = bounce(turt) #bounces, if at a wall
    
    if didBounce:
        count +=1
    
    # Terminating condition
    if count >= 50:
        run = False
        
panel.mainloop()
turtle.done()        

