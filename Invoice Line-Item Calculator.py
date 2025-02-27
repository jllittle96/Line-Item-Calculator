def get_price():
    while True:
        try:
            price = input("\nEnter price: ")
            if "," in price:
                raise ValueError  # Only a period is allowed for decimal numbers
            price = float(price)
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = input("Enter quantity: ")
            quantity = int(quantity)  # Checking for integer input
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity

        print(f"\nPRICE:\t  {price:.2f}")
        print(f"QUANTITY:  {quantity}")
        print(f"TOTAL:\t  {total:.2f}\n")

        another = input("Enter another line item? (y/n): ").strip().lower()
        if another != 'y':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()