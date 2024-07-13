n = input()

width = 0

def insert_into_center(original, insert):
    middle_index = len(original) // 2
    return original[:middle_index] + insert + original[middle_index:]

for i in range(n):

    l = []

    if n % 2 == 0:
        width = n-1
    else:
        width = n

    line = []
    for j in range(width):
        
        
