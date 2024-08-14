LAB = "turtlelab1.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab1 import turtle,check

turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(50)
check()