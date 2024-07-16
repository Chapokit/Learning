n = input()

a = list(map(int, input().split()))
a = sorted(a)

no_zeroes = []
number_of_zeroes = 0

for i in a:
    if i == 0:
        number_of_zeroes += 1
    else:
        no_zeroes.append(i)

for i in range(number_of_zeroes):
    no_zeroes.insert(i+1,0)
    
print("".join(map(str, no_zeroes)))