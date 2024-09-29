'''
Greedy_Snake.py 1.2.2版本
***优化了部分代码
***修正了边界问题的bug
'''
from random import randrange
import gamebase
import turtle

def initialize():
    turtle.title("Greedy Snake")
    turtle.bgcolor("lightblue")
    turtle.setup(420,420,0,0)
    turtle.listen()
    
    global X, Y
    global moveX, moveY, moveX2, moveY2
    global Snake, Snake2
    global m, n, crush
    X = randrange(-15,15)*10
    Y = randrange(-15,15)*10
    moveX = 10
    moveY = 0
    moveX2 = -10
    moveY2 = 0
    Snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
    Snake2 = [[0,0],[-10,0],[-20,0],[-30,0],[-40,0],[-50,0]]
    n = 0
    m = 0
    crush = 0


    #bind all keys
    turtle.onkey(lambda: change(0,10),"w")
    turtle.onkey(lambda: change(-10,0),"a")
    turtle.onkey(lambda: change(0,-10),"s")
    turtle.onkey(lambda: change(10,0),"d")

    turtle.onkey(lambda: change2(0,10),"Up")
    turtle.onkey(lambda: change2(-10,0),"Left")
    turtle.onkey(lambda: change2(0,-10),"Down")
    turtle.onkey(lambda: change2(10,0),"Right")


def snakecrush():
    for crush in range(len(Snake)-1):
       if Snake[-1] == Snake[crush]:
           return True

def snakecrush2():
    for crush in range(len(Snake2)-1):
       if Snake2[-1] == Snake2[crush]:
           return True
       
def inside():
    if Snake[-1][0] >= 190 or Snake[-1][1] >= 200 or Snake[-1][0] <= -210 or Snake[-1][1] <= -200:
        return True
    
def inside2():
    if Snake2[-1][0] >= 190 or Snake2[-1][1] >= 200 or Snake2[-1][0] <= -210 or Snake2[-1][1] <= -200:
        return True
    
def change(x,y):
    global moveX,moveY
    if moveX != x and moveY != -y:
        moveX = x
        moveY = y 

def change2(x,y):
    global moveX2,moveY2
    if moveX2 != x and moveY2 != -y:
        moveX2 = x
        moveY2 = y

def GameLoop():
    global X,Y
    Snake.append([Snake[-1][0] + moveX,Snake[-1][1] + moveY])
    if inside():
        return
    if snakecrush():
        return
    if not (X == Snake[-1][0] and Y == Snake[-1][1]):
        Snake.pop(0)
        turtle.clear()
    else:
        X = randrange(-15,15)*10
        Y = randrange(-15,15)*10
    gamebase.square(-210,-200,410,"black")
    gamebase.square(-200,-190,390,"white")
    gamebase.square(X,Y,10,"green")
    for n in range(len(Snake)):
        gamebase.square(Snake[n][0],Snake[n][1],10,"blue")
        n = n+1
    
    if playerNum == 2:
        Snake2.append([Snake2[-1][0] + moveX2,Snake2[-1][1] + moveY2])
        if inside2():
            return
        if snakecrush2():
            return
        if not (X == Snake2[-1][0] and Y == Snake2[-1][1]):
            Snake2.pop(0)
        else:
            X = randrange(-15,15)*10
            Y = randrange(-15,15)*10
        for m in range(len(Snake2)):
            gamebase.square(Snake2[m][0],Snake2[m][1],10,"red")
            m = m+1
    turtle.ontimer(GameLoop,speed)


if __name__ == "__main__":
    playerNum = int(input("单人版(W A S D)请输入'1'，双人版(上下左右)请输入'2':"))
    speed = int(input("速度选择(50快 100中速 200慢):"))
    initialize()
    GameLoop()
    turtle.done()  
