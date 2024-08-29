LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/%7BLAB%7D.0",LAB)

from turtlelab3 import turtle,home,check

from math import degrees,atan

distance = (home.x2 + home.y2)**0.5
angle = degrees(atan(abs(home.y/home.x)))
turtle.left(180 - angle)
turtle.forward(distance)

check()
