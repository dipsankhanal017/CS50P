import random


cards = ['A♠️','A♣️','A♦️','A♥️','2♠️','2♣️','2♦️','2♥️','3♠️','3♣️','3♦️','3♥️','4♠️','4♣️','4♦️','4♥️','5♠️','5♣️','5♦️','5♥️','6♠️','6♣️','6♦️','6♥️','7♠️','7♣️','7♦️','7♥️','8♠️','8♣️','8♦️','8♥️','9♠️','9♣️','9♦️','9♥️','10♠️','10♣️','10♦️','10♥️','J♠️','J♣️','J♦️','J♥️','Q♠️','Q♣️','Q♦️','Q♥️','K♠️','K♣️','K♦️','K♥️']

hearts= [ card for card in cards if "♥️" in card]

def main():
    deck = cards
    random.shuffle(deck)
    player1, player2, player3, user = [deck[i:i+13] for i in range(0, len(deck), 13)]
    p1Hand = generateHands(player1)
    p2Hand = generateHands(player2)
    p3Hand = generateHands(player3)
    userHand = int(input("Your target hands: "))
    play(player1, player2, player3, user)



    #print(player1,p1Hand,player2,p2Hand,player3,p3Hand,user,userHand, sep = "\n")

def generateHands(cards):
    hand = 0
    for card in cards:
        if "♠️" in card:
            try:
                if int(card.replace("♠️","")) > 5: hand +=1
            except ValueError:
                hand +=1
        if "A" in card and "♠️" not in card: hand +=1
        if "K" in card and "♠️" not in card: hand +=1
    if hand == 0: hand = 1
    return hand



def play(p1, p2, p3, user):
    print(user)
    c1 = user[int(input("Throw a card: "))]
    user.remove(c1)
    c2 = throwCards(c1, p1)
    print(c2)
    print(p1)

def throwCards(x, cards):
    print(x[1])
    if len(x) == 2: sign = x[1]
    if len(x) == 3: sign = x[2]
    print(sign)
    new_list = [c for c in cards if sign in c]
    return new_list

if __name__ == "__main__":
    main()
