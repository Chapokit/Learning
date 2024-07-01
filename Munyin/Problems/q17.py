a, b = map(int, input().split())

numbers = list(range(a+1))[2:]
removed = list(range(a+1))[2:]
order = 0

for x in numbers:
    for y in numbers:
        if y%x == 0 and y in removed:
            removed.remove(y)
            order += 1
        if order == b:
            answer = y
            order += 1

print(answer)