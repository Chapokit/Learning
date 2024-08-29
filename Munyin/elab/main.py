LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.2", LAB)


from turtlelab3 import turtle, home, check

from math import degrees,atan

distance = (home.x**2 + home.y**2)**0.5
angle = degrees(atan(abs(home.y/home.x)))
turtle.right(angle)
turtle.forward(distance)