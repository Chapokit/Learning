data = [('Germany', 6), ('Ghana', 4), ('Serbia', 3), ('Australia', 3)]

# Get the scores
points = [score for country, score in data]

# Find duplicates
output = [score if points.count(score) > 1 else 'x' for score in points]

print(output)
