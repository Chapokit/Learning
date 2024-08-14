n = int(input("num: "))

if n%2 == 0:
    n1 = int(n/2)
    n2 = n1
else:
    n1 = int(n/2) + 1
    n2 = n - n1
print(n1,n2)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
answer = factorial(n)/(factorial(n1)*factorial(n2))
if n == 1:
    print(2)
else:
    print(int(answer))