
def calculate_change(charge, payment):
    return payment-charge

def read_all_inputs():

    name = input("Please enter your name: ")
    charge = float(input("Please enter your charge: "))
    payment = float(input("Please enter your payment: "))

    return name, charge, payment

def find_change_in_bills(change):
    
    FIVEHUNDRED = 0
    HUNDRED = 0
    TWENTY = 0
    while change >= 500:
        change -= 500
        FIVEHUNDRED += 1
    while change >= 100:
        change -= 100
        HUNDRED += 1
    while change >= 20:
        change -= 20
        TWENTY += 1
    coins = change

    return FIVEHUNDRED,HUNDRED,TWENTY,coins

def show_change(FIVEHUNDRED,HUNDRED,TWENTY,coins):
    print(f"You will receive {FIVEHUNDRED} 500-Baht bills, {HUNDRED} 100-Baht bills, {TWENTY} 20-Baht bills, and {coins:.2f} Baht change in coins.")


name, charge, payment = read_all_inputs()
change = calculate_change(charge, payment)
a,b,c,d = find_change_in_bills(change)
print(f"Hello, {name}.  Thank you for visiting.")
print(f"Your change is {change:.2f} Baht.")
print(show_change(a,b,c,d))
