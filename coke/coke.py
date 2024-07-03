cokePrice = 50

while cokePrice != 0:
    print("Amount Due:", cokePrice)
    while True:
        insertCoin = int(input("Insert Coin: "))
        if insertCoin == 25 or insertCoin == 10 or insertCoin == 5:
            break
        else:
            print("Amount Due:", cokePrice)
    cokePrice -= insertCoin
    if cokePrice < 0:
        break

print("Change Owed:", abs(cokePrice))
