country = {}
score = []

for i in range(4):
    a = input("Enter country: ")
    country[a] = 0


for i in range(4):
    scores = input(f"Enter scores for {list(country.keys())[i]}: ").split()
    score.append(list(map(int, scores))) 

countries = list(country.keys())

for i in range(4):
    for j in range(4):
        if i == j:
            continue  
        if score[i][j] > score[j][i]:
            country[countries[i]] += 3

goal_delta = []

for i in range(4):

    row_sum = sum(score[i])
    col_sum = sum(score[j][i] for j in range(4))
    goal_delta.append(row_sum-col_sum)




sorted_country = sorted(country.items(), key=lambda item: item[1])
for country_name, score in sorted_country[::-1]:
    print(f"{country_name} {score}")

