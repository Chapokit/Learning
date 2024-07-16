def round_or_not(num):
# use if-else here

   decimal_part = str(num).split(".")

   if len(decimal_part) > 1 and len(decimal_part[1]) > 0:
        first_digit = int(decimal_part[1][0])
        if first_digit > 5:
            print(int(decimal_part[0])+1)
        else:
            print(decimal_part[0])

# input here
user_num = input("What is your number? ")

round_or_not(user_num)
