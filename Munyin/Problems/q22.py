n = 4
width = 0

def center(original, insert):
    middle_index = len(original) // 2
    return original[:middle_index] + insert + original[middle_index:]

if n % 2 == 0:
    width = n - 1
else:
    width = n

for i in range(n):
    line = "-" * (width - 1)

    if i == 0:
        line = center(line, "*")

    print(line)  # Output the result