from plates import is_valid
def main():
    test_isValid()

def test_isValid():
    assert is_valid("AAAAA") == True
    assert is_valid("AAA555") == True
    assert is_valid("01234") == False
    assert is_valid("A") == False
    assert is_valid("AA,AA") == False
    assert is_valid("3AAAA") == False
    assert is_valid("AAA055") == False
    assert is_valid("11111") == False
    assert is_valid("A555A") == False
    assert is_valid("CS50P") == False
if __name__ == "__main__":
    main()
