burger_list = []
burger = {"top": "bun", "middle 1": "cheese", "middle 2": "meat", "bottom": "bun"}

for key, value in enumerate(burger.items()):
    burger_list.append(value)



burger_list = burger_list[::-1]
burger.clear()
print(f"The dict should be blank by now: {burger}")
print(f"WOW BURGER: {burger_list}")
print()


burger['middle 2'] = "banana"
print("Heh, Banana hamburger")
print(f"Current state of burger: {burger}")
print(f"Are your list: {burger_list} empty?")