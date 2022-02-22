import turtle
t=turtle.Turtle()
range=float(input("Nhập ban kinh xoan oc: "))
d=10
t.speed(2)
t.home()
a=t.position()
while t.distance(a)<range:
    t.circle(d,50)
    d+=1
turtle.done()