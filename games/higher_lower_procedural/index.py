import random

SUIT_TUPLE = ('Spades','Hearts','Diamonds','Clubs')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

print('Welcome to Higher or Lower')
print('You have to choose wheter the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank,'suit':suit,'value':thisValue+1}
        startingDeckList.append(cardDict)

# print(startingDeckList)
score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCard = getCard(gameDeckList)
    currentCardRank = currentCard['rank']
    currentCardSuit = currentCard['suit']
    currentCardValue = currentCard['value']
    
    print('Starting card is: {} of {}'.format(currentCardRank,currentCardSuit))
    
    for cardNumber in range(0, NCARDS):
        answer = input('Will the next card be higher or lower than the current card? (h/l) ')
        print(f"This is your {cardNumber} change ")
        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        
        print('Next card is: {} of {}'.format(nextCardRank,nextCardSuit))
        
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score += 20
            else :
                print('You got it wrong, it was lower')
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower')
                score += 20 
            else :
                print('You got it wrong, it was higher')
                score -= 15
        print('Your score is {}'.format(score))
        print()
        currentCardRank  = nextCardRank
        currentCardValue = nextCardValue
    
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    
    if goAgain == 'q':
        break
print('Thanks for playing')