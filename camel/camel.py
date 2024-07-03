x = input("camelCase: ")
i = 0

while i < len(x):
    if x[i].isupper():
        a, b = x.split(x[i])
        b = x[i].lower() +  b
        x = a+"_"+b
        i = i-1
    i = i + 1
print("snake_case:",x)
