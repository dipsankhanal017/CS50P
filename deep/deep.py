x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace("-", " ").strip()

if x == "42" or x == "forty two":
    print("Yes")
else:
    print("No")
