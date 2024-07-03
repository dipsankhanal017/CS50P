from tabulate import tabulate
import csv
import sys

def main():
    checkCommandLen()
    fname = sys.argv[1]
    checkFileType(fname)
    data = getList(fname)
    print(tabulate(data, tablefmt="grid", headers = "keys"))

def getList(fname):
    data = []
    with open(fname) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
def checkCommandLen():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

def checkFileType(fname):
    if ".csv" not in fname:
        print("Not a CSV file")
        sys.exit(1)


if __name__ == "__main__":
    main()
