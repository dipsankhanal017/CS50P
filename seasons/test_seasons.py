from seasons import Age
import sys
def main():
    testAge()
    sys.exit(0)

def testAge():
    assert Age.calculate("2023-03-11") == "Five hundred twenty-seven thousand forty minutes"
    assert Age.calculate("2022-03-11") == "One million, fifty-two thousand, six hundred forty minutes"





if __name__ == "__main__":
    main()
