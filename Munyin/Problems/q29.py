a,b = map(float, input().split())

a = int(a)
b = int(b)

q,n = divmod(b,a)

if n > 0:
    print(q+1)
else:
    print(q)