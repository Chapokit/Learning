#Global variables
TWENTY = 20
HUNDRED = 100
FIVEHUNDRED = 500



def read_all_inputs():
    name = input("Please enter your name: ")
    charge = float(input("Please enter your charge: "))
    payment = float(input("Please enter your payment: "))
    return name, charge, payment


def calculate_change(charge, payment):
    change = payment - charge
    return change


def find_change_in_bills(change):
    bills_500 = change // FIVEHUNDRED
    change = change - bills_500 * 500
    bills_100 = change // HUNDRED
    change = change - bills_100 * 100
    bills_20 =change // TWENTY
    change = change - bills_20 * 20
    coins = change
    return bills_500, bills_100, bills_20, coins


def show_change(name, change, bills_500, bills_100, bills_20, coins):
    print(f'Hello, {name}. Thank you for visiting.')
    print(f'Your change is {change:.2f} Baht.')
    print(f'You will receive {int(bills_500)} 500-Baht bills, {int(bills_100)} 100-Baht bills, {int(bills_20)} 20-Baht bills, and {coins:.2f} Baht change in coins.')


name, charge, payment = read_all_inputs()
change = calculate_change(charge, payment)
bills_500, bills_100, bills_20, coins = find_change_in_bills(change)
show_change(name, change, bills_500, bills_100, bills_20, coins)
