import re
import sys

def main():
    print(convert(input("Hours: ").strip()))
    sys.exit(0)

def convert(s):
    if a := re.match("^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$", s):
        h1 = int(a.group(1))
        m1 = a.group(2)
        t1 = a.group(3)
        h2 = int(a.group(4))
        m2 = a.group(5)
        t2 = a.group(6)

        if t1 == "PM": h1 = h1 + 12
        if t2 == "PM": h2 = h2 + 12

        if m1 is None: m1 = "00"
        if m2 is None: m2 = "00"

        if h1 == 24 : h1 = 12
        if h2 == 24 : h2 = 12

        if h1 < 10: h1 = "0" + str(h1)
        if h2 < 10: h2 = "0" + str(h2)

        if h1 == 12 and t1 == "AM" : h1 = "00"
        if h2 == 12 and t2 == "AM" : h2 = "00"

        return f"{h1}:{m1} to {h2}:{m2}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
