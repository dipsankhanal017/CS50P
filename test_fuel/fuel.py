# main.py

def main():
    n = input("Fraction: ")
    try:
        n = convert(n)
        if 1 < n < 99:
            print(f"{n}%")
        else:
            print(gauge(n))
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")

def convert(value):
    try:
        a, b = value.split("/")
        x = int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        raise
    x = round(x, 2)
    return int(x * 100)

def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return f"{x}%"
