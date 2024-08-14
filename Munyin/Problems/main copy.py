import math

x = int(input("Enter value of x: "))
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

def change_log_base(x,a,b):
    return math.log(x,b)/math.log(a,b)

print(f"Logarithm of {x:.3f} with base {a:.3f} = {math.log(x,a):.3f}")
print(f"Logarithm of {x:.3f} with base {b:.3f} / Logarithm of {a:.3f} with base {b:.3f} = {change_log_base(x,a,b):.3f}")