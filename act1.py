import turtle
e=int(input("Write the number of sides: "))
a=turtle.Turtle()
b=turtle.Screen()
c=70
d=360/e
b.bgcolor("orange")
b.setup(300,400)
a.color("blue")
a.shape("classic")
for i in range(e):
    a.forward(c)
    a.right(d)
a.hideturtle()
turtle.done()
    
    
    
