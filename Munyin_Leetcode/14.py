strs = ["flower","flow","flight"]
shortest_string = min(strs, key=len)
length = len(strs) - 1
strs = [s for s in strs if s != shortest_string]

ans = []

for word in strs:
    word = list(word)
    for i in range(len(shortest_string)):

        if shortest_string[i] == word[i]:
            if shortest_string not in ans:
                ans.append(word[i])

char_count = {}

for char in ans:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


duplicates = [char for char, count in char_count.items() if count == length]

result_string = ''.join(duplicates)

print(result_string)