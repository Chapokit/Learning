import math
def get_input():
    done = False
    all_value = []
    while done == False:
        value = input("Input score (or just ENTER to end): ")
        if value != "":
            all_value.append(float(value))
        else:
            done = True
    return all_value
    

value_list = get_input()
average_score = sum(value_list) / len(value_list)
print(f"Average score is {average_score:.2f}")
sigma_value = 0

for i, value in enumerate(value_list):
    sigma_value += (value - average_score)**2
    
# print(sigma_value)
SD = math.sqrt((sigma_value) / (len(value_list)-1) )
print(f"Standard deviation is {SD:.2f}")

for i, value in enumerate(value_list):
    grade = ""
    if value >= average_score + 1.5*SD:
        grade = "A"
    elif value >= average_score + SD and value < average_score + 1.5*SD:
        grade = "B+"
    elif value >= average_score + 0.5*SD and value < average_score + SD:
        grade = "B"
    elif value >= average_score and value < average_score + 0.5*SD:
        grade = "C+"
    elif value >= average_score - 0.5*SD and value < average_score:
        grade = "C"
    elif value >= average_score - SD and value < average_score -0.5*SD:
        grade = "D+"
    elif value >= average_score - 1.5*SD and value < average_score - SD:
        grade = "D"
    elif value < average_score - 1.5*SD:
        grade = "F"

    print(f"Score #{i+1}: {value:.0f} grade: {grade}")
