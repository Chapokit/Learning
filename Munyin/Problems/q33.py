n = input()
l = map(int, input().split())

value_dict = {}

for index, value in enumerate(l):
    value_dict[value] = value_dict.setdefault(value, 0) + 1

highest_value = max(value_dict.values())
highest_keys = sorted([key for key, value in value_dict.items() if value == highest_value])
print(" ".join(map(str, highest_keys)))