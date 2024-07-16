country = {"Germany": 0, "Serbia": 0, "Australia": 0, "Ghana": 0}
score = [[0, 0, 4, 1], [1, 0, 1, 0], [0, 2, 0, 1], [0, 1, 1, 0]]

countries = list(country.keys())

for i in range(4):
    for j in range(4):
        if i == j:
            continue  
        if score[i][j] > score[j][i]:
            country[countries[i]] += 3

goal_delta = []
goals = []
for i in range(4):

    row_sum = sum(score[i])
    col_sum = sum(score[j][i] for j in range(4))
    goal_delta.append(row_sum-col_sum)
    goals.append(row_sum)

print(sorted(country.items(), key=lambda item: item[1], reverse=True))
print(goal_delta)
print(goals)

point = []
for i in range(4):
    if i != 0:
        if country[countries[i-1]] == country[countries[i]]:
            point.append(country[countries[i]])
        else:
            point.append("x")
    if i == 3:
        if len(point) > 1:
            point.append(point[2])

print(point)


l = []
for i,points in enumerate(point):

    if isinstance(points, int):
        print(goal_delta[i])
        l.append(goal_delta[i])
    else:
        l.append('x')

print(l)
only_num = []
for i,number in enumerate(l):

    if isinstance(number, int):
        only_num.append(number)

print(max(only_num))
plus_one = l.index(max(only_num))
print(plus_one)

country[countries[plus_one]] += 1
print(sorted(country.items(), key=lambda item: item[1], reverse=True))



points = list(country.values())

output = [score if points.count(score) > 1 else 'x' for score in points]

print(output)