from numb3rs import validate
def main():
    test_validate()

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("0.1.1.255") == True
    assert validate("1.1.555.1") == False

if __name__ == "__main__":
    main()

