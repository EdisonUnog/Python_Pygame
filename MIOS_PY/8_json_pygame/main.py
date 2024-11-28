
from turtle import*
import colorsys
bgcolor("gray")
tracer(10)
pensize(5)
h = 0
for i in range(400):
    c = colorsys.hsv_to_rgb(h,1, 1)
    h += 0.005
    pencolor(c)
    fillcolor("black")
    begin_fill()
    for j in range(2):
        fd(i*1.2)
        rt(60)
        fd(300)
        rt(120)
    rt(121)
    end_fill()
done()





