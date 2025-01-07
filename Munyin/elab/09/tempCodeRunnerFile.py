txt = input("Enter a string: ")

for i in range(len(txt)):
    print(f"{i*" "}{txt[i]}")