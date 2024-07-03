import emoji

a = input("Input: ")
if "earth_asia" in a:
    a = a.replace(":earth_asia:", "🌏")
    print("Output:", a)
elif ":thumbsup:" in a:
    a = a.replace(":thumbsup:", "👍")
    print("Output:", a)
else:
    print("Output:", emoji.emojize(a))
