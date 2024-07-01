n = "bapas jepe doposapadnapa opovapa kepemipijapa"
new_word = []
skip_next = 0
vowels = ["a", "e", "i", "o", "u"]

for count, letter in enumerate(n):
    if skip_next > 0:
        skip_next -= 1
        continue

    if letter in vowels:
        skip_next = 2 
        new_word.append(letter)
    else:
        new_word.append(letter)

print(''.join(new_word))