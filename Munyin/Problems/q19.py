# n = int(input())
# ingre = []

# for i in range(n):
#     ingre.append(list(map(int,input().split())))

ingre = [1, 3, 10]

ingre_count = ingre[0]
ingre.remove(ingre_count)
sour = ingre[0::2]
bitter = ingre[1::2]
best = 1000000000

def diff(x,y):
    
    return y - x if x < y else x - y

def recur(i, sourness, bitterness):
    if i == ingre_count:
        if bitterness > 0 and diff(sourness, bitterness) < best:
            best = diff(sourness, bitterness)
    else:
        recur(i + 1, sourness, bitterness)
        recur(i + 1, sourness * sour[i], bitterness + bitter[i])
    
recur(0, 1, 0)

print(best)


