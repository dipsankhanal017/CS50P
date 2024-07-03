import random


def main():
    level = get_level()
    num = generate_integer(level)
    c = 0
    for _ in range(10):
        x = random.choice(num)
        y = random.choice(num)
        k = 0
        while True:
            z = int(input(f"{x} + {y} = "))
            if x+y == z:
                c +=1
                break
            else:
                print("EEE")
                k +=1
                if k == 3:
                    print(x + y)
                    break
    print("Score:",c)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n == 1 or n == 2 or n == 3:
                return n

def generate_integer(level):
    match level:
        case 1:
            return range(10)
        case 2:
            return range(10, 100)
        case 3:
            return range(100, 1000)

if __name__ == "__main__":
    main()

