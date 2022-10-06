import turtle

def curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        curve(size / 3, n - 1)
        turtle.left(60)
        curve(size / 3, n - 1)
        turtle.right(120)
        curve(size / 3, n - 1)
        turtle.left(60)
        curve(size / 3, n - 1)
def main(size, n):
    myWin = turtle.Screen()
    for i in range(3):
        curve(size, n)
        turtle.right(120)
    myWin.exitonclick()

main(300, 3)