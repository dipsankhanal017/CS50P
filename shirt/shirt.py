import sys
from PIL import Image, ImageOps

def main():
    checkCommandLine()
    checkExtension(sys.argv[1], sys.argv[2])
    overLay(sys.argv[1], sys.argv[2])

def checkCommandLine():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

def checkExtension(before, after):
    ext = [".jpg", ".jpeg", ".png"]
    i = 0
    while i < 3:
        if ext[i] in before or ext[i] in after:
            break
        else:
            i += 1
    if i == 3:
        print("Invalid output")
        sys.exit(1)

    if before[-3:] != after[-3:]:
        print("Input and output have different extensions")
        sys.exit(1)


def overLay(before, after):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before) as img:
            before1 = ImageOps.fit(img, shirt.size)
            before1.paste(shirt, mask = shirt)
            before1.save(after)
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
