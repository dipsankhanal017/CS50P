from working import convert
import sys

def main():
    test_convert()


def test_convert():
    try:
        assert convert("9 AM to 5 PM") == "09:00 to 17:00"
        assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
        assert convert("12 PM to 12 AM") == "12:00 to 00:00"
        assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    except ValueError:
        sys.exit(1)


if __name__ == "__main__":
    main()
