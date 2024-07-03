def main():
    x = input("Input: ")
    print("Output:",shorten(x))
def shorten(x):
    x = x.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    x = x.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")
    return x

if __name__ == "__main__":
    main()
