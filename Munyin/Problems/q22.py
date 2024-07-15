n = 4

def insert(text,pos):

    inserted = text[:pos] + "*" + text[pos:]
    return inserted

if n % 2 == 0:
    width = n - 1
else:
    width = n

for i in range(n):
    if i==0 or i==(width-1):
        line = "-" * (width - 1)
        print(insert(line,(width//2)))
    
    for j in range(width):
        pass


