from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("4/5") == 80
    with pytest.raises(ValueError):
        convert("c/at")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    main()
