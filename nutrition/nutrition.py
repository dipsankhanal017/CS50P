fruitName = input("Item: ").lower()

match fruitName:
    case "apple":
        cal = 130
    case "avocado":
        cal = 50
    case "banana":
        cal = 110
    case "cantaloupe":
        cal = 50
    case "grapefruit":
        cal = 60
    case "grapes":
        cal = 90
    case "honeydew melon":
        cal = 50
    case "kiwifruit":
        cal = 90
    case "lemon":
        cal = 15
    case "lime":
        cal = 20
    case "nectarine":
        cal = 60
    case "orange":
        cal = 80
    case "peach":
        cal = 60
    case "pear":
        cal = 100
    case "pineapple":
        cal = 50
    case "plums":
        cal = 70
    case "strawberries":
        cal = 50
    case "sweet cherries":
        cal = 100
    case "tangerine":
        cal = 50
    case "watermelon":
        cal = 80
    case _:
        cal = 0
if cal > 0:
    print("Calories:",cal)
else:
    print("", end="")
