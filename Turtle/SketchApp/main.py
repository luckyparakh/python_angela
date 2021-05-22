from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def forward():
    tim.forward(5)


def backward():
    tim.backward(5)


def cw():
    tim.right(5)


def acw():
    tim.left(5)

def sclear():
    tim.clear()
    tim.reset()

screen.onkey(forward, "a")
screen.onkey(backward, "s")
screen.onkey(cw, "q")
screen.onkey(acw, "w")
screen.onkey(sclear, "c")
screen.listen()
screen.exitonclick()
