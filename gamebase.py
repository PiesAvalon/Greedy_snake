from turtle import *
def square(x,y,size,color_name):
    hideturtle()
    tracer(False)
    up()
    goto(x,y)
    color(color_name)
    n=0
    begin_fill()
    while n<4:
        forward(size)
        left(90)
        n=n+1

    end_fill()
    
