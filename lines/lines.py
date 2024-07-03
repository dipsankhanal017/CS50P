import sys

if len(sys.argv) == 2:
    if ".py" in sys.argv[1]:
        fname = sys.argv[1]
    else:
        print("Not a Python file")
        sys.exit(1)
else:
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        print("Too few command-line arguments")
    sys.exit(1)


c = 0
try:
    with open(fname) as file:
        for line in file:
            line = line.strip()
            if line != "" and line[0] != "#":
                c += 1
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
print(c)
