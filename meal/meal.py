def main():
    time = input("What time is it? ")
    x = convert(time)

    if 7.0 <= x <= 8.0:
        print("breakfast time")
    elif 12.0 <= x <= 13.0:
        print("lunch time")
    elif 18.0 <= x <= 19.0:
        print("dinner time")


def convert(time):
    a , b = time.split(":")
    c = float(a) + (float(b)/60.0)
    return c

if __name__ == "__main__":
    main()

