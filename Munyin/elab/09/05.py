hours = int(input("Enter numbers of hours: "))

for i in range(hours):
    print(f"In {i+1} hour(s), my factory produces {180*(i+1)} candies, and I make profit of {72*(i+1) :.2f} Baht.")