import sys
import csv

def main():
    checkCommandline()
    newData = readFile(sys.argv[1])
    writeFile(newData, sys.argv[2])

def checkCommandline():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

def readFile(fname):
    data =[]
    try:
        with open(fname) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit(1)

    newData1 = []
    for ele in data:
        newData = {}
        newData["last"], firstName = ele["name"].split(",")
        newData["first"] = firstName.strip()
        newData["house"] = ele["house"]
        newData1.append(newData)
    return newData1


def writeFile(data, fname):
    with open(fname, "w") as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for value in data:
            writer.writerow(value)

if __name__ == "__main__":
    main()
