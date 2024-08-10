import math

n = 5
width = n - (n % 2)
center = math.ceil(n/2)
print(center) # 3

def make_line():
    
    x = 0
    for i in range(n):
        l = ""
        for j in range(n):
            print(j)
            if i == 0:
                if j + 1 == center:
                    l += "*"
                else:
                    l += "-"
            else:
                if j == center + x + 1:
                    l += "*"
                elif j == center - x + 1:
                    l += "*"
                else:
                    l += "-"
            x += 1
        
        print(l)


make_line()




