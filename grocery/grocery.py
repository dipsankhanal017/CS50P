def main():
    items = getItems()
    single = sorted(list(set(items)))
    i = 0
    while i < len(single):
        n = items.count(single[i])
        print(n, single[i].upper())
        i += 1

def getItems():
    collection = []
    try:
        while True:
            items = input()
            collection.append(items)
    except EOFError:
        return collection

main()
