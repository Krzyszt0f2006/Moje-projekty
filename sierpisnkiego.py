import turtle
#turtle.setx(-50)
#turtle.sety(-50)
turtle.speed(0)
def trojkat():
    m=300
    for i in range(3):
        turtle.forward(m)
        turtle.left(120)
    #1
    turtle.forward(m/2)
    turtle.left(120)
    for i in range(2):
        turtle.forward(m/2)
        turtle.right(120)
    turtle.forward(m/2)
    turtle.left(120)
    #2
    turtle.forward(m/4)
    turtle.left(120)


def sierpinskiego(dl,gl):
    if gl==0:
        for i in range(3):
            turtle.forward(dl)
            turtle.left(120)
    else:
        sierpinskiego(dl//2,gl-1)
        turtle.forward(dl//2)
        sierpinskiego(dl // 2, gl - 1)
        turtle.back(dl//2)
        turtle.left(60)
        turtle.forward(dl//2)
        turtle.right(60)
        sierpinskiego(dl // 2, gl - 1)
        turtle.left(60)
        turtle.back(dl//2)
        turtle.right(60)
def choinka():
    turtle.pensize(5)
    turtle.teleport(-400,-300)
    turtle.color("green")
    sierpinskiego(250,4)
    turtle.forward(250/3+20)
    turtle.color("sienna4")
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.color("green")
    #turtle.forward(60)
    #turtle.back(250/3+20+60)
    #turtle.right(-90)
    #turtle.forward(200)
    #turtle.right(90)
    turtle.teleport(-360,-84)
    sierpinskiego(175,3)
    turtle.teleport(-335,65)
    sierpinskiego(120,2)
    turtle.pensize(2)
def tlo():
    turtle.teleport(-1000,-1000)
    turtle.color('SteelBlue1')
    turtle.begin_fill()
    turtle.sety(1000)
    turtle.setx(1000)
    turtle.sety(-1000)
    turtle.end_fill()
tlo()
choinka()
turtle.color("red")

turtle.teleport(100,-330)
turtle.begin_fill()
def prezent():
    for i in range(4):
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()
prezent()
def napis():
    turtle.teleport(-400,300)
    turtle.write('wesolych swiat',False,"Left",font=('Arial', 46, 'normal'))
napis()

#trojkat()
turtle.done()