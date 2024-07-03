def main():
    d = getDate("Date: ")
    if "/" in d:
        print(newFormat1(d))
    elif "," in d:
        print(newFormat2(d))

def getDate(prompt):
    while True:
        date = input(prompt)
        if "/" in date:
            a, b, c = date.split("/")
            try:
                a = int(a)
                b = int(b)
            except ValueError:
                pass
            else:
                if a <= 12 and b <= 31:
                    break
        elif "," in date:
            m, n = date.split(",")
            o, p = m.split(" ")
            try:
                p = int(p)
            except ValueError:
                pass
            if o in months and p <= 31:
                break
    return date

def newFormat1(date1):
    a1, b1, c1 = date1.split("/")
    a1 = int(a1)
    b1 = int (b1)
    c1 = c1.strip()
    if a1 < 10:
        a1 = "0" + str(a1)
    if b1 < 10:
        b1 = "0" + str(b1)
    abc = c1 + "-" + str(a1) + "-" + str(b1)
    return abc

def newFormat2(date2):
    m1, n1 = date2.split(",")
    o1, p1 = m1.split(" ")
    n1 = n1.strip()
    q1 = months.index(o1)
    p1 = int(p1)
    if q1 < 10:
        q1 = "0" + str(q1)
    if p1 < 10:
        p1 = "0" + str(p1)
    abc1 = n1 + "-" + str(q1) + "-" + str(p1)
    return abc1


months = [
    " ",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

main()
