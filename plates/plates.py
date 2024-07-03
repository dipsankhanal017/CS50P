def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return checkF2Letters(s) and checkLength(s) and checkNoPosition(s) and checkPSP(s)

def checkF2Letters(s):
    return s[:2].isalpha()

def checkLength(s):
    return 2 <= len(s) <= 6

def checkNoPosition(s):
    i = 0
    if s.isalpha():
        return True
    while i < len(s):
        j = i-len(s)
        if i>2:
            if s[i].isdigit():
                if s[i] == 0:
                    return False
                elif s[-j:].isdigit():
                    return True
                
        i +=1


def checkPSP(s):
    if any(char in ". ,;:!?" for char in s):
        return False
    else:
        return True

main()
