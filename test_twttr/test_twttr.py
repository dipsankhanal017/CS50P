from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"
    assert shorten("CAT") == "CT"
    assert shorten("apple, BALL and 5 cats") == "ppl, BLL nd 5 cts"

if __name__ == "__main__":
    main()
