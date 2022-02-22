import turtle
t=turtle.Turtle()
t.speed(0.5)
rad = 0
while rad <6:
    for color in ('red','aqua','green','coral','yellow','fuchsia','brown','khaki','sky blue','orange','dark blue','navy'):
        t.color(color)
        count=0
        while count<2:
            t.circle(200,90)
            t.circle(80,90)
            count+=1
        t.right(5)
    rad +=1
    
turtle.done()