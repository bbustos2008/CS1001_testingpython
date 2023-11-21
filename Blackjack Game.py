import random
playerwins = 0
dealerwins = 0
playerIn = True
dealerIn = True

#deck of cards / player dealer hand
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["diamonds", "spades", "clubs", "hearts"]
playerhand = []
dealerhand = []

class card:
    def __init__(self,r,s):
        self.rank = r
        self.suit = s

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def getvalue(self):
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

deck = []
for r in ranks:
    for s in suits:
        deck.append(card(r,s))

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
        total = total + card.getvalue()
    return total     

def showhand(hand):
    ret = ''
    first = True
    for c in hand:
        if not first:
            ret = ret + ','
        ret = ret + str(c)
        if first:
            first = False
    return ret

#check for winner
def dealerchoice():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]
    
f = open("gamescore.txt","r")
contents = f.readline()
parts = contents.split(":")
playerwins = int(parts[0].strip())
dealerwins = int(parts[1].strip())
f.close()

# game loop
for _ in range(2):
    dealcards(dealerhand)
    dealcards(playerhand)

HitorStay = '1'
while playerIn and dealerIn:
    print(f"dealer has {dealerhand[0]}, X")
    print(f"you have {showhand(playerhand)} for a total of {total(playerhand)}")
    if playerIn and HitorStay == '1':
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
     

print(f"dealer has {showhand(dealerhand)} for a total of {total(dealerhand)}")
print(f"you have {showhand(playerhand)} for a total of {total(playerhand)}")

if total(playerhand) == 21 and len(playerhand) == 2:
    print("Blackjack!")
    playerwins = playerwins + 1
elif total(dealerhand) == 21 and len(dealerhand) == 2:
    print("Dealer has blackjack. You lose!")
    dealerwins = dealerwins + 1
elif total(dealerhand) == total(playerhand):
    print("Tie goes to the dealer. You lose!")
    dealerwins = dealerwins + 1
elif total(playerhand) > 21:
    print("You Bust!")
    dealerwins = dealerwins + 1
elif total(dealerhand) > 21:
    print("Dealer busts. You win!")
    playerwins = playerwins + 1
elif total(dealerhand) > total(playerhand):
    print("dealer wins")
    dealerwins = dealerwins + 1
elif total(playerhand) > total(dealerhand):
    print("you win")
    playerwins = playerwins + 1

print(f"Score: Player - {playerwins} Dealer - {dealerwins}")

f = open("gamescore.txt","w")
f.write(f"{playerwins}:{dealerwins}")
f.close()