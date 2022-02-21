import turtle
import math
t=turtle.Turtle()
r=int(input("Nhap ban kinh hinh tron: "))
t.hideturtle()
t.pensize(2)
t.color("green")
t.circle(r)
c=2*math.pi*r
s=math.pi*r*r
print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))