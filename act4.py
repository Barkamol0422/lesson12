import turtle as a
d=a.Turtle()
e=a.Screen()
e.bgcolor("blue")
d.shape("classic")
b=int(input("Write the number of sides: "))
c=int(input("Write the length of sides: "))
f=360/b
for i in range(b):
    d.forward(c)
    d.right(f)
a.done()
