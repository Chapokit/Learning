scores = []
for i in range(5):
  line = input()
  scores.append(list(map(int, line.split())))


max_score = 0
winner = 0

for i in range(5):
  total_score = sum(scores[i])
  if total_score > max_score:
    max_score = total_score
    winner = i + 1

print(f"{winner} {max_score}")
