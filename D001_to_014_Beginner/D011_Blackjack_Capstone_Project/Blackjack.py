import os, random
from Blackjack_Art import logo

def deal(target, number=1):
    '''Deal the target a number of cards, one by default.'''
    for i in range(number):
        target.append(random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))

def score_check(hand):
    '''If the supplied hand is 21 with two cards, mark it as a Blackjack. If it's over 21, turn an ace from an 11 to a 1.'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    elif sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def winner(user, dealer):
    '''Use the user and dealer's scores to determine the winner of the hand.'''
    if dealer == 0:
        print('The dealer got a blackjack, too bad!')
    elif user == 0:
        print('You got a blackjack, congratulations!')
    elif user <= 21 and user > dealer:
        print('Your score is higher than the dealer\'s, congratulations!')
    elif user > 21:
        print('You bust! Too bad!')
    elif dealer > 21:
        print('The dealer busts! Congratulations!')
    elif user == dealer:
        print('You tie with the dealer!')
    else:
        print('The dealer\'s score is higher than yours, too bad!')
    
def play():
    '''Set up the starting position, let the user draw, determine victor once the player goes over 21 or voluntarily stops drawing.'''
    user = []
    dealer = []
    deal(user, 2)
    deal(dealer, 2)

    # If neither user has 21 by default, continue on with the game.
    if not (sum(user) == 21 or sum(dealer) == 21):
        while score_check(user) < 21:
            os.system('cls||clear')
            print(logo)
            print(f'User\'s Cards: {user} total {sum(user)}')
            print(f'Dealer\'s First Card: [{dealer[0]}]')
            if input('\nWould you like to be dealt another card? [Y/N] ').upper() == 'Y':
                deal(user)
            else:
                break

    # Once the player is done drawing without busting, have the dealer draw until they're at or above 17.
    while sum(dealer) < 17:
        deal(dealer)
        score_check(dealer)

    # Display the results of the game. Blackjack, win, bust, tie, etc. and the final scores.
    os.system('cls||clear')
    print(logo)
    print(f'User\'s Cards: {user} total {sum(user)}')
    print(f'Dealer\'s Cards: {dealer} total {sum(dealer)}\n')
    winner(score_check(user), score_check(dealer))

    # Let the user choose to play again, looping back to the start of this function. Otherwise, exit entirely.
    while True:
        replay = input('Play again? [Y/N] ').upper()
        if replay == 'Y':
            play()
        elif replay == 'N':
            print('Thanks for playing Blackjack!')
            exit()

# Play the game. The functions will do the rest.
play()