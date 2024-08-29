import math

def read_vector(text):
    print(text)
    x = float(input("Input value of x: "))
    y = float(input("Input value of y: "))
    return x, y

def dot_product(x1, y1, x2, y2):
    x = x1*x2
    y = y1*y2
    product = x+y
    return product

def convert_vector_to_str(x1, y1):
    return f"[{x1:.2f}, {y1:.2f}]"

x1, y1 = read_vector("For vector A")
x2, y2 = read_vector("For vector B")
product = dot_product(x1, y1, x2, y2)
val1 = convert_vector_to_str(x1, y1)
val2 = convert_vector_to_str(x2, y2)
print(f"Dot product of {val1} and {val2} is {product:.2f}")