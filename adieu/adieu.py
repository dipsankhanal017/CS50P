def main():
    A = getNames()
    adieu(A)

def getNames():
    A = []
    try:
        while True:
            A.append(input("Name: "))
    except EOFError:
        pass
        return A


def adieu(A):
    print()
    print("Adieu, adieu, to", end=" ")
    for x in A:
        if (A.index(x)+1) == (len(A)-1):
            if len(A) == 2:
                print(x, end = " and ")
            else:
                print(x, end = ", and ")
        elif (A.index(x)+1) == len(A):
            print(x)
        else:
            print(x, end = ", ")

main()
