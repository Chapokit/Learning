import math

REGULAR_PRICE = 100
SENIOR_PRICE = 25
KID_PRICE = 50
IMAX_PRICE = 100
DRINK_PRICE = 20

def read_guests():

    total_guest = int(input("Enter #guests in total: "))
    seniors = int(input("Enter #seniors: "))
    children = int(input("Enter #children: "))

    return total_guest, seniors, children

def read_services():

    IMAX_ticket = int(input("Enter #IMAX tickets: "))
    drink_voucher = int(input("Enter #drink vouchers: "))

    return IMAX_ticket, drink_voucher

def calculate_price(numbers_item=0,item_price=0):
    
    return numbers_item * item_price

def calculate_total_ticket_price(total_guests=1, seniors=0, children=0):

    normal = total_guests - (seniors+children)
    seniors_price = calculate_price(seniors, SENIOR_PRICE)
    kid_price = calculate_price(children, KID_PRICE )
    regular_price = calculate_price(normal, REGULAR_PRICE)

    return regular_price + seniors_price + kid_price

def show_ticket_summary(total_guests, seniors, children):

    normal = total_guests - (seniors+children)
    seniors_price = calculate_price(seniors, SENIOR_PRICE)
    kid_price = calculate_price(children, KID_PRICE )
    regular_price = calculate_price(normal, REGULAR_PRICE)

    print("Ticket Summary:")
    print(f"{seniors} senior tickets cost {seniors_price:.2f} Baht.")
    print(f"{children} children tickets cost {kid_price:.2f} Baht.")
    print(f"{normal} general tickets cost {regular_price:.2f} Baht.")

def get_purchase_summary_str(total_ticket_price, num_IMAX, drink_voucher):
    
    imax = num_IMAX*IMAX_PRICE
    drink = drink_voucher*DRINK_PRICE
    total = total_ticket_price + imax + drink
    return (
    f"Purchase Summary:\n"
    f"Total tickets cost {total_ticket_price:.2f} Baht.\n"
    f"Total IMAX tickets cost {imax:.2f} Baht.\n"
    f"Total drink vouchers cost {drink:.2f} Baht.\n"
    f"Total payment cost {total:.2f} Baht."
)

total_guest, seniors, children = read_guests()
num_IMAX, drink_voucher = read_services()
total = calculate_total_ticket_price(total_guest, seniors, children)
show_ticket_summary(total_guest, seniors, children)
print(get_purchase_summary_str(total, num_IMAX, drink_voucher))

print()
print(get_purchase_summary_str(1900,5,4))