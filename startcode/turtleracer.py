import turtle
import random
class TurtleRacer:
    def __init__(self,kleur, index):
        self.kleur = kleur
        self.index = index
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(self.kleur)
        self.turtle.penup()
        self.turtle.goto(-200, 200-(index * 30))
        self.turtle.pendown()

    def race(self):
        snelheid = random.randint(1, 25)
        self.turtle.forward(snelheid)

racers = [
    TurtleRacer("red", 1),
    TurtleRacer("blue", 2),
    TurtleRacer("green", 3)
    ]

for i in range(25):
    for racer in racers:
        racer.race()
turtle.done()