#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import random

num_wins = [0, 0, 0, 0, 0]#list of number of wins each racer has

racers = [] #emptly list of racers
colors = ['red', 'yellow', 'green', 'blue', 'orange']#colors/names for each racer
turtle.screensize(500, 500)#screensize

def setup():
    '''Sets up the distance markings'''
    s = turtle.Turtle()
    
    s.penup()
    s.setpos(-400, -480) #positioning the pen

    for sp in range(22): #loop for creating the lines labelled with numbers
        s.speed(20)
     #setting the speed
        s.write(sp)
     #writing the int
        s.forward(40)
     #forward at 10 units
        s.pendown()
     #ready to draw
        s.forward(175*5)
     #forward at 150 units
        s.penup()
     #not ready to draw
        s.backward(175*5+40)
     #back at 160 units
        s.left(90)
     #left set at 90 degrees
        s.forward(40)
     #forward at 20 units
        s.right(90)
     #setting right at 90 degrees

def create_track():
    '''Creates the track each racer will race in'''
    artist = turtle.Turtle()#creating artist turtle
    artist.speed(15)
    artist.right(90)
    
    x = [-350, -184, -18, 148, 314]#x, pos of each of the tracks
    y = 500
    
    for i, color in enumerate(colors):#create each track based on color
        artist.penup()
        artist.color(color)
        artist.setpos(x[i], y)
        artist.pendown()
        artist.forward(990)
        artist.left(90)
        artist.forward(32)
        artist.left(90)
        artist.forward(990)
        artist.left(180)

    artist.penup()
    artist.color('black')
    artist.setpos(-500, 400)
    x, y = artist.pos()
    artist.left(90)
    while x < 500:
        x, y = artist.pos()
        artist.pendown()
        artist.forward(25)
        artist.penup()
        artist.forward(25)
    #^^^ Creates the finish line
    
'''RacerPositions
-334 -480
-168 -480
-2 -480
164 -480
330 -480'''


space = 1000//(len(colors) + 1)#space between each racer
def create_racer():
    '''creates racers in a list'''
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-1000//2 + (i+1) * space, -1000//2 + 20)
        racer.pendown()
        racer.speed(15)
        racers.append(racer)

def reset_racer():
    '''resets racer position'''
    for i, racer in enumerate(racers):
        racer.penup()
        racer.setpos(-1000//2 + (i+1) * space, -1000//2 + 20)
        racer.pendown()
        

def race():
    '''Starts the race between each color racer'''
    while True:
        for racer in racers:
            racer.fd(random.randrange(5, 30))
            x, y = racer.pos()
            if y >= (1000 // 2) - 100:
                num_wins[racers.index(racer)] += 1
                return colors[racers.index(racer)], num_wins[racers.index(racer)]           

def write(winner, wins):
    '''writes the number of wins for each color in a text file named winnersfile.txt'''
    with open('winnersfile.txt', 'w') as f:
        
        for x, i in enumerate(colors):
            if i == winner:
                f.write(i +' = '+ str(num_wins[x]) + '\n')
            else:
                f.write(i +' = '+ str(num_wins[x]) + '\n')

#---Calling functions 
setup()
create_track()
create_racer()
while input('Press y to continue: ') == 'y':
    winner, wins = race()
    write(winner, wins)
    for x in racers:
        x.clear()#clears the board/track
    reset_racer()


# In[ ]:


import turtle
import random
import math

win = turtle.Screen()#initializes turtle screen
p = turtle.Turtle() #turtle #1
p1 = turtle.Turtle() #turtle #2
p1.shape('turtle')
p.shape('turtle')
win.bgcolor('aqua')#sets background color
p1.speed(50)
p.speed(10)

#Draws grass
p1.color('light green')
p1.penup()
p1.setpos(-650,-300)
p1.pendown
p1.begin_fill()
for x in range(2):
    p1.forward(1300)
    p1.right(90)
    p1.forward(300)
    p1.right(90)
p1.end_fill()

#positions turtle
p.color('light green', 'green')
p.penup()
p.left(90)
p.forward(25)
p.begin_fill()
p.right(90)
p.forward(25)
p.pendown()
#draws the stem for the flower
p.begin_fill()
for x in range(2):
    p.right(90)
    p.forward(500)
    p.right(90)
    p.forward(50)
p.end_fill()
#brings back to origin
p.penup()
p.home()
p.pendown()


#sets up turtle for drawing clouds
cld = turtle.Turtle()
cld.color('white', 'white')
cld.speed(15)

def cloud(x, y, r):
    '''Draws a cloud wih arguments x, y for position and r for max radius of cloud'''
    cld.penup()
    cld.setpos(x, y)
    cld.pendown()
    cld.begin_fill()
    for x in range(2):
        for x in range(3):
            cld.penup()
            cld.forward(random.randrange(40, 70))
            cld.pendown()
            cld.circle(random.randrange(25,r))
            cld.left(random.randrange(45,115))     
    cld.end_fill()

def flw(n):
    '''Draws a flower with arguments n for number of pedals'''
    f = turtle.Turtle()
    f.shape('turtle')
    turtle.colormode(255)#switches color mode to between 0 and 255 for rgb
    f.speed(50)
    f.setpos(0,50)#positions in the middle of the flower
    for x in range(n):
        #Randomly chooses an angle to start drawing a pedal
        c = random.randrange(1,3)
        if c == 1:
            f.left(random.randrange(float(360)))
        if c == 2:
            f.right(random.randrange(float(360)))
        #sets the color to a random value
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        f.pencolor(r, g, b)
        f.fillcolor(r, g, b)
        #draws the pedal
        f.begin_fill()
        for x in range(3):
            f.forward(random.randrange(25,125))#random amount to go forward
            r = random.randrange(1,3)#random angle to turn for 'curve'
            if r == 1:
                f.left(random.randrange(10,55))
            if r == 2:
                f.right(random.randrange(5,45))
        f.setpos(0,50)#resets/finishes fill
        f.end_fill()
#draws four clouds and 50 flower pedals  
cloud(-375, 300, 75)
cloud(310, 350, 80)
cloud(-5, 375, 60)
cloud(400, 150, 40)
flw(100)

#draws the center of the flower
p.color('black', 'brown')
p.begin_fill()
p.circle(40)
p.end_fill()

