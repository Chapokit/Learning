def calculate_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return area

n = int(input())
coor = []

for i in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))

highest_area = 0.00

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = calculate_area(coor[i], coor[j], coor[k])
            if area > highest_area:
                highest_area = area

print(f"{highest_area:.3f}")
