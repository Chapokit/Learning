country = {"Denmark": 0, "Netherlands": 0, "Cameroon": 0, "Japan": 0}
score = [[0, 0, 2, 1], [2, 0, 2, 1], [1, 1, 0, 0], [3, 0, 1, 0]]

countries = list(country.keys())
# print(countries)

for i in range(4):
    for j in range(4):
        if i == j:
            continue  
        if score[i][j] > score[j][i]:           
            country[countries[i]] += 3


# print(country)

sorted_country = sorted(country.items(), key=lambda item: item[1])
for country, score in sorted_country[::-1]:
    print(f"{country} {score}")


