from bank import value
def main():
    test_value()

def test_value():
    assert value("Hello") == 0
    assert value("How are you?") == 20
    assert value("Good morning") == 100

if __name__ == "__main__":
    main()
