N = 10
question = "ABCABCABCABC"

def Adrain():
    correct = 0
    pattern = "ABC"
    for count, answer in enumerate(question):
        if answer == pattern[count % 3]:
            correct += 1
    return correct

def Bruno():
    correct = 0
    pattern = "BABC"
    for count, answer in enumerate(question):
        if answer == pattern[count % 4]:
            correct += 1
    return correct

def Goran():
    correct = 0
    pattern = "CCAABB"
    for count, answer in enumerate(question):
        if answer == pattern[count % 6]:
            correct += 1
    return correct

people = {
    "Adrain": Adrain(),
    "Bruno": Bruno(),
    "Goran": Goran()
}

highest_score = max(people.values())
highest_scorers = sorted([person for person, score in people.items() if score == highest_score])

print(highest_score)
for person in highest_scorers:
    print(person)

print(people)