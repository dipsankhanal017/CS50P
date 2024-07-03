def main():
    price = 0.00
    while True:
        try:
            item = input("Item: ").lower()
            if getPrice(item) != 0.00:
                price += float(getPrice(item))
                newPrice = f"{price:.2f}"
                print("Total:", newPrice, sep=" $")
        except EOFError:
            break

def getPrice(item):
    match item:
        case "baja taco":
            return 4.25
        case "burrito":
            return 7.50
        case "bowl":
            return 8.50
        case "nachos":
            return 11.00
        case "quesadilla":
            return 8.50
        case "super burrito":
            return 8.50
        case "super quesadilla":
            return 9.50
        case "taco":
            return 3.00
        case "tortilla salad":
            return 8.00
        case _:
            return 0.00

if __name__ == "__main__":
    main()
