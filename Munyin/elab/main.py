LAB = "turtlelab3x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3x import turtle,home,shop,check
import math
from math import atan, degrees, sqrt

distance1 = math.sqrt( (shop.x)**2 + (shop.y)**2 )
angle = degrees(atan(abs((shop.y/shop.x))))
turtle.left(angle)
turtle.forward(distance1)

turtle.right(angle)

distance2 = math.sqrt( (home.x-shop.x)**2 + (home.y-shop.y)**2 )
angle = degrees(atan(abs(((home.y-shop.y) / (home.x-shop.x)))))
turtle.left(angle)
turtle.forward(distance2)
