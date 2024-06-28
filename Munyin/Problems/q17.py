# a, b = map(int, input().split())
a = 10
b = 7

numbers = list(range(a+1))[2:]
numbers2 = list(range(a+1))[2:]
order = 0

for prime in numbers:
    for number in numbers:
        if number%prime == 0 and number in numbers:
            numbers2.remove(number)
            order += 1
        if order == b:
            answer = number
            order+=1
print(answer)
