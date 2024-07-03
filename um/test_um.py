from um import count

def main():
    test_count()
    sys.exit(1)

def test_count():
    assert count("hello, um, yo") == 1
    assert count("hello, um, Um cat") == 2
    assert count("yummy") == 0


if __name__ == "__main__":
    main()
