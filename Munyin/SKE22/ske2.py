time_that_occur = []
user_tuple = (True, False, None, True, True, True, False)

# These codes are not efficient. You will learn better methods to handle this question on Day 3.

# Find how many times each value occurs in the tuple.
time_that_occur.append(
user_tuple.count(user_tuple[0])
)
time_that_occur.append(
user_tuple.count(user_tuple[1])
)
time_that_occur.append(
user_tuple.count(user_tuple[2])
)
time_that_occur.append(
user_tuple.count(user_tuple[3])
)

user_tuple = list(user_tuple)


position_of_most_occur_value = time_that_occur.index(max(time_that_occur))


target_value= user_tuple[position_of_most_occur_value]

for i in range(len(user_tuple)):
    if user_tuple[i] == target_value:
        user_tuple[i] = "Banana"

print(
user_tuple
)