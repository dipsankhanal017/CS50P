import random
def main():
    level = getLevel("Level: ")
    rNum = random.choice(range(1, level+1, 1))
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > rNum:
                print("Too large!")
            elif guess < rNum:
                print("Too small!")
            elif guess == rNum:
                print("Just right!")
                exit()

def getLevel(prompt):
    while True:
        try:
            level = int(input(prompt))
        except ValueError:
            pass
        else:
            if level > 0: return level


main()
