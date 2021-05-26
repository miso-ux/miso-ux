import lib2to3.pgen2.token
import random
import socketserver
import turtle
import time
def stvorec(kor: turtle.Turtle, posx: int = 0, posy: int = 0) -> None:
    kor.penup()
    kor.setpos(posx, posy)
    kor.pendown()
    kor.pencolor()
    for _ in range(4):
        kor.forward(100)
        kor.left(90)
korytnacka = turtle.Turtle()
for _ in range(200):
    px = random.randint(-200, 200)
    py = random.randint(-200, 200)
    stvorec(korytnacka, px, py)
turtle.mainloop()

# t = turtle.Turtle()
# t.color("green")
# t.shape("turtle")
# for _ in range(4):
#    t.left(90)
#    t.forward(100)
# turtle.mainloop()
# time.sleep(5)
