cash = int(input("Enter cash in Baht: "))
years = int(input("Enter n years: "))
profit = 0
for i in range(years):
    total_and_profit = cash * ((1 + 1.5/100)**(i+1))   
    print(f"You will get back {total_and_profit:.2f} Baht in {i+1} years.")
    profit = total_and_profit
if years == 0:
    print(f"At the end, you will earn 0.00 Baht of interest in {years} years.")
else:
    print(f"At the end, you will earn {profit-cash:.2f} Baht of interest in {years} years.")