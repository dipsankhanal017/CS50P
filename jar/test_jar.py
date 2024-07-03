from jar import Jar
jar = Jar()
def main():
    testDeposit()
    testWithdraw()
    testCapacity()
    testSize()

def testDeposit():
    jar.deposit(5)
    assert jar.size == 5

def testWithdraw():
    jar.withdraw(1)
    assert jar.size == 4

def testCapacity():
    assert jar.capacity == 12

def testSize():
    assert jar.size == 4


if __name__ == "__main__":
    main()
