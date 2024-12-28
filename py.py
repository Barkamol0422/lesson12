import turtle
a=turtle.Turtle()
b=turtle.Screen()
b.bgcolor("light blue")
c=0
while True:
    for i in range(4):
        a.fd(c+1)
        a.left(90)
        c=c-5
    c=c+1
