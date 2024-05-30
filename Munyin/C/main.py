word = "ABCD"
s = "#"

first = ""
second = ""
third = ""

length = len(word)

for count, character in enumerate(word):
    if (count+1)%3 != 0 and count != 0:
        first += ".#.."
        second += ".#.#"
        third += f"#.{character}."
        s = "#"       
    elif count == 0:
        first += ".#.."
        second += ".#.#"
        third += f"#.{character}."
        s = "#"
    elif (count+1) %3 == 0:
        first += ".*.."
        second += ".*.*"
        third += f"*.{character}."
        s = "*"

print(f".{first}")
print(f"{second}.")
print(f"{third}{s}")
print(f"{second}.")
print(f".{first}")



