FIVEHUNDRED = 0
HUNDRED = 0
TWENTY = 0

def read_all_inputs():

    name = input("Please enter your name: ")
    charge = float(input("Please enter your charge: ")) 
    payment = float(input("Please enter your payment: ")) 
    return name, charge, payment

def calculate_change(charge, payment):
    change = payment-charge
    return change

def find_change_in_bills(change):

    global FIVEHUNDRED, HUNDRED, TWENTY 

    FIVEHUNDRED = change // 500
    change %= 500
    
    HUNDRED = change // 100
    change %= 100
    
    TWENTY = change // 20
    coins = change % 20
    
    return FIVEHUNDRED, HUNDRED, TWENTY, coins

def show_change(name, change, FIVEHUNDRED, HUNDRED, TWENTY, coins):
    print(f"Hello, {name}.  Thank you for visiting.")
    print(f"Your change is {change:.2f} Baht.")
    print(f"You will receive {FIVEHUNDRED:.0f} 500-Baht bills, {HUNDRED:.0f} 100-Baht bills, {TWENTY:.0f} 20-Baht bills, and {coins:.2f} Baht change in coins.")

name, charge, payment = read_all_inputs()
change = calculate_change(charge, payment)
FIVEHUNDRED, HUNDRED, TWENTY, coins = find_change_in_bills(change)
show_change(name, change, FIVEHUNDRED, HUNDRED, TWENTY, coins)