def to_list(string):
    # l = []
    # for letter in string:
    #     if letter != " " and letter != ",":
    #         l.append(letter)
    # return l
    return [name for name in string.split() if name]

def to_str(list_value):

    list_value = map(str, list_value)
    l = []
    for letter in list_value:
        if letter not in (" ", ",", "[", "]", '"'):

            l.append(letter)
    answer = " ".join(l)
    
    return answer

list_or_str = input("Should the value be turned into a list or a string? ")
user_input = input("What value would you like to convert? ")
list_or_str = list_or_str.upper()  # Assign the uppercase result back
if list_or_str == "STR":
    print(to_str(eval(user_input)))
elif list_or_str == "LIST":
    print(to_list(user_input))
else:
    pass
