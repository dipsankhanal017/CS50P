def main():
    n = getFraction("Fraction: ")
    if isinstance(n, int):
        print(n, "%", sep = "")
    else:
        print(n)

def getFraction(prompt):
    while True:
        try:
            a, b = input(prompt).split("/")
            if int(a) <= int(b):
                try:
                    x = int(a)/int(b)
                    if x >= 0.99:
                        return "F"
                    elif x <= 0.01:
                        return "E"
                    else:
                        break
                except ZeroDivisionError:
                    pass
        except ValueError:
            pass
    x = round(x, 2)
    return int(x*100)

main()
