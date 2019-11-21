import turtle
from YassinFunction import*
bob.speed(100)

bob.color("blue")
bob.begin_fill()
for times in range(60):
    bob.forward(80)
    bob.left(6)
bob.right(80)
bob.end_fill()

jump(500,-130)
bob.left(90)
bob.color("purple")
bob.begin_fill()
for times in range(60):
    bob.forward(80)
    bob.right(6)
bob.end_fill()


jump(-900,-100)
bob.color("Yellow")
bob.begin_fill()
for times in range(60):
    bob.forward(80)
    bob.right(6)
bob.end_fill()

bob.color("cyan")
jump(0,0)


for times in range(50):
    c = (0,0,times*5)
    polygon(8,200-times*3,c)
    bob.right(times)
