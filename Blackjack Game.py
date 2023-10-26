import random
playerIn = True
dealerIn = True
#deck of cards / player dealer hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerhand = []
dealerhand = []

#class card:
    #def __init__(self,r,s):
        #self.rank = r
        #self.suit = s

#class deck:
    #def __init__(self):
        #self.cards = []

    #def shuffle(self):
        #print("do nothing")

    #def draw(self):
        #print("do nothing")

    #def addcard(self,card):
       #self.cards.append(card)

#ranks = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#suits = ["diamonds", "spades", "clubs", "hearts"]

#deck = deck()
#for r in ranks:
    #for s in suits:
        #c = card(r,s)
        #deck.dealcards(c)
        


#deal cards
def dealcards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate total of each hand
def total(turn):
    total = 0
    face = ['J','Q','K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11    
    return total               

#check for winner
def dealerchoice():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]

# game loop
for _ in range(2):
    dealcards(dealerhand)
    dealcards(playerhand)
HitorStay = 1
while playerIn and dealerIn:
    print(f"dealer has {dealerhand}")
    print(f"you have {playerhand} for a total of {total(playerhand)}")
    if playerIn and HitorStay == 1:
        HitorStay = input(" Choose 1: hit or 2: stay")
    if total(dealerhand) > 16:
        dealerIn = False
    else:
        dealcards(dealerhand)
    if HitorStay == "2":
        playerIn = True
    else: 
       dealcards(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerhand) >= 21:
        break

print(f"dealer has {dealerhand} for a total of {total(dealerhand)}")
print(f"you have {playerhand} for a total of {total(playerhand)}")

if total(playerhand) == 21 and len(playerhand) == 2:
    print("Blackjack!")
elif total(dealerhand) == 21 and len(dealerhand) == 2:
    print("Dealer has blackjack. You lose!")
elif total(dealerhand) == total(playerhand):
    print("Tie goes to the dealer. You lose!")
elif total(playerhand) > 21:
    print("You Bust!")
elif total(dealerhand) > 21:
    print("Dealer busts. You win!")
elif total(dealerhand) > total(playerhand):
    print("dealer wins")
elif total(playerhand) > total(dealerhand):
    print("you win")