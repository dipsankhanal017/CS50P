import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    if (a := re.search(r'<iframe\s+src="https?://(?:www\.)?youtube\.com/embed/([^"]+)".*?</iframe>', s)) or (a := re.search(r'^<iframe src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"></iframe>$', s)):
        return f"https://youtu.be/{a.group(1)}"
    else:
        return None




if __name__ == "__main__":
    main()
