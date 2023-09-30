import random
import sys

HEARTS   = chr(9829) # Character 9829 is '♥'
DIAMONDS = chr(9830) # Character 9830 is '♦'
SPADES   = chr(9824) # Character 9824 is '♠'
CLUBS    = chr(9827) # Character 9827 is '♣'
BACKSIDE = 'backside'

def main():
    print('''
Welcome to BlackJack          

Rules:
    Try to get as close to 21 without going over.
    - Kings, Queens, and Jacks are worth 10 points.
    - Aces are worth 1 or 11 points.
    - Cards 2 through 10 are worth their face value.
    
    (H)it to take another card.
    (S)tand to stop taking cards.
    
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.'''
    )

    money = 5000
    bet = 0
    while True:
        if money <= 0:
            print("You're broke!")
            sys.exit()

        print("Money: ", money)
        bet = getBet(money)
    
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet: ', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to ', bet)
                print('Bet: ', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                playerHand.append(newCard)
                print('You drew a {} of {}'.format(rank, suit))

                if getHandValue(playerHand) > 21:
                    continue
            
            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break

                input('Press ENTER to continue...')
                print('\n\n')

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print('Dealer busts. You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost ${}'.format(bet))
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie! The bet is returned to you')

        input('Press ENTER to continue...')
        print('\n\n')
        
        
def getBet(money):
    while True:
            print("How much you want to bet? (1 - {} or QUIT)".format(money))
            bet = input('> ').upper().strip()
            if bet == "QUIT":
                print("Thanks for playing!")
                sys.exit()

            if not bet.isdecimal():
                continue

            bet = int(bet)
            if 1 <= bet <= money:
                return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, HEARTS):
        for rank in range (2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((str(rank), suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE] + dealerHand[1:])

    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(hand):
    value = 0
    numberOfAces = 0

    for card in hand:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range (numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['','','','','']
    for i, card in enumerate(cards):
        rows[0] = ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '| # | '
            rows[3] += '| ##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '| {}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble Down')
        
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble Down' in moves:
            return move


if __name__ == '__main__':
    main()