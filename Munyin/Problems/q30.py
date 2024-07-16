a = int(input())
answer = []
q,n = divmod(a,3)
answer.append(n)
q,n = divmod(a,11)
answer.append(n)


print(" ".join(map(str, answer)))