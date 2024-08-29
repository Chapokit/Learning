n = int(input("number: "))

l = []

for i in range(n):
    square = input("Go: ")
    subset = []
    for i in square:
        subset.append(i)
    l.append(subset)

blank = l

for i in range(n):

    q_index = []

    for j in range(n):
        if l[i][j] == 'Q':
            q_index.append(j)

    if len(q_index) >= 2:
        for j in q_index:
            l[i][j] = '-'

for i in range(n):

    q_index = []

    for j in range(n):
        if l[j][i] == 'Q':
            q_index.append(j)

    if len(q_index) >= 2:
        for j in q_index:
            l[j][i] = '-'

for i in range(n):

    q_index = []

    for j in range(n):
        if l[j][j] == 'Q':
            q_index.append(i)

    if len(q_index) >= 2:
        for j in q_index:
            l[i][i] = '-'
        
print(l)