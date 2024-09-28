from random import randrange
from turtle import *
from time import sleep
from gamebase import *

X = randrange(-200,200)
Y = randrange(-200,200)
Snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
n = 0
def GameLoop():

    for n in range(len(Snake)):
        square(Snake[n][0],Snake[n][1],10,"black")
        n = n+1

    square(X,Y,10,"blue")

setup(420,420,0,0)
GameLoop()
done()