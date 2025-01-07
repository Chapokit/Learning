
done = False
num = []
while not done:
    score = input("Input score (or just ENTER to end): ")
    if score == '':
        done = True
    else:
        num.append(float(score))

num.sort(reverse=True)

for i, value in enumerate(num):
    print(f"Rank #{i+1}: {value:.0f}")