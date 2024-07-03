def main():
    x = input("Greeting: ")
    print("$",value(x), sep = "")


def value(x):
    if  "Hello" in x:
        return 0
    elif x[0] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
