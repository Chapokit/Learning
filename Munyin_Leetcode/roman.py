n = "MCMXCIV"
number_list = [char for char in n]
number_list = number_list[::-1]  # Reverse the list
print(number_list)

val = 0
skip = 0

for index, sym in enumerate(number_list):
    if skip != 0:
        skip -= 1
        pass
    else:
        if sym == "I":
            val += 1
        elif sym == "V":
            val += 5

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "I":
                    val -= 1
                    skip += 1
                else:
                    break
        elif sym == "X":
            val += 10

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "I":
                    val -= 1
                    skip += 1
                else:
                    break
        elif sym == "L":
            val += 50

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "X":
                    val -= 10
                    skip += 1
                else:
                    break
        elif sym == "C":
            val += 100

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "X":
                    val -= 10
                    skip += 1
                else:
                    break
        elif sym == "D":
            val += 500

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "C":
                    val -= 100
                    skip += 1
                else:
                    break
        elif sym == "M":
            val += 1000

            for preceding_sym in number_list[index + 1:]:
                if preceding_sym == "C":
                    val -= 100
                    skip += 1
                else:
                    break
    

print(val)  # Should print 2
