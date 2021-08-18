import random
# from random import randrange
from typing import List
from graphics import *






win = GraphWin("Tournament", 600, 500,)
win.setBackground("light blue")
partrecta = Rectangle(Point(0, 0), Point(125, 200))
partrecta.setFill("pink")
firstline = Line(Point(150, 100), Point(250, 100))
seconline = Line(Point(150, 200), Point(250, 200))
thirdline = Line(Point(250, 100), Point(250, 200))
fourtline = Line(Point(150, 300), Point(250, 300))
fifthline = Line(Point(150, 400), Point(250, 400))
sixthline = Line(Point(250, 300), Point(250, 400))
sevenline = Line(Point(250, 150), Point(350, 150))
eightline = Line(Point(250, 350), Point(350, 350))
ninthline = Line(Point(350, 150), Point(350, 350))
tenthline = Line(Point(350, 250), Point(450, 250))
message = Text(Point(60, 10), "Participants: ")
firstline.draw(win)
seconline.draw(win)
thirdline.draw(win)
fourtline.draw(win)
fifthline.draw(win)
sixthline.draw(win)
sevenline.draw(win)
eightline.draw(win)
ninthline.draw(win)
tenthline.draw(win)
partrecta.draw(win)
message.draw(win)

print("!!!Currently supports 4 players only.!!!")
print("Input Players Names: ")
playero = input("First: ")
plaero = Text(Point(50, 35), playero)
plaero.draw(win)
playert = input("Second: ")
plaert = Text(Point(50, 60), playert)
plaert.draw(win)
playerf = input("Third: ")
plaerf = Text(Point(50, 85), playerf)
plaerf.draw(win)
playerc = input("Fourth: ")
plaerc = Text(Point(50, 110), playerc)
plaerc.draw(win)

people = [playero, playert, playerf, playerc]

randtes = random.sample(range(4), 4)

# print(randtes)

person1 = people[randtes[0]]
person2 = people[randtes[1]]
person3 = people[randtes[2]]
person4 = people[randtes[3]]

# print(person1)
# print(person2)
# print(person3)
# print(person4)

teamone = [person1, person2]
teamtwo = [person3, person4]
teamthr = []

plaero = Text(Point(170, 90), person1)
plaero.draw(win)
plaero = Text(Point(170, 190), person2)
plaero.draw(win)
plaero = Text(Point(170, 290), person3)
plaero.draw(win)
plaero = Text(Point(170, 390), person4)
plaero.draw(win)





print("First fight is '" + person1 + "' VS '" + person2 + "'.")
firstlos = input("Who lost? ")
teamone.remove(firstlos)
print("Winner is: ")
print(teamone[0])

plaero = Text(Point(310, 140), teamone[0])
plaero.draw(win)

print("Second Fight is '" + person3 + "' VS '" + person4 + "'.")
seconlos = input("Who lost? ")
teamtwo.remove(seconlos)
print("Winner is: ")
print(teamtwo[0])
teamthr.append(teamone[0])
teamthr.append(teamtwo[0])


plaero = Text(Point(310, 340), teamtwo[0])
plaero.draw(win)

print("Final Fight is " + teamone[0] + " VS " + teamtwo[0] + ".")
winr = input("Who lost? ")
teamthr.remove(winr)
plaery = Text(Point(410, 240), teamthr[0])
plaery.draw(win)
print("The winner overall was: " + teamthr[0] + "!")

loefuadb = input("Exit Now? (Yes): ")