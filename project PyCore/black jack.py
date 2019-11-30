from random import *

name = input('Input your name: ')
print('Hello, {}!'.format(name))
print("It's a Black Jack game realised on python3. Enjoy!")
input('Press Enter to start! ')
print('=' * 10)


def check_21(hand):
    return sum(hand) > 21


def check_bj(hand):
    return hand == 21


def list_to_string(list_of_var):
    return ', '.join(list_of_var)


def game_check(dealer_value, player_value):
    return player_value > dealer_value


def ace_changer(hand):
    for ace in hand:
        if (ace == 11 and check_21(hand)):
            ace_pos = hand.index(11)
            hand[ace_pos] = 1
    return hand


def game_construct(player_hand, dealer_hand):
    if check_21(dealer_hand):
        if sum(player_hand) <= 21:
            player_score = 1
            dealer_score = 0
    if check_21(player_hand):
        if sum(dealer_hand) <= 21:
            dealer_score = 1
            player_score = 0
            print('Too mutch!')
    if not check_21(player_hand) and not check_21(dealer_hand):
        if sum(player_hand) > sum(dealer_hand):
            player_score = 1
            dealer_score = 0
        else:
            dealer_score = 1
            player_score = 0
    if check_bj(player_hand):
        player_score = 1
        dealer_score = 0
    if check_bj(dealer_hand):
        dealer_score = 1
        player_score = 0
    if check_bj(player_hand) and check_bj(dealer_hand):
        dealer_score = 1
        player_score = 0
    if check_21(player_hand) and check_21(dealer_hand):
        player_score = 0
        dealer_score = 0
    return player_score, dealer_score


def game_loop(name):
    player_win = 0
    dealer_win = 0
    play_again = 'yes'
    while play_again.lower()[0] == 'y':
        player_hand, player_hand_type = player_turn()
        dealer_hand, dealer_hand_type = dealer_turn()
        player_score, dealer_score = game_construct(player_hand, dealer_hand)
        result_of_round(name, player_hand, player_hand_type,
                        dealer_hand, dealer_hand_type)
        if player_score > dealer_score:
            print('{} win!'.format(name))
            player_win += 1
        elif player_score < dealer_score:
            print('Dealer win!')
            dealer_win += 1
        else:
            print('Tie!')
        print('=' * 10)
        play_again = input('Do you want to continue (y/n)? ')
    return player_win, dealer_win


def take_card():
    card_list = ['10', 'J', 'Q', 'K']
    card_value = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4)
    if card_value == 10:
        card_type = choice(card_list)
    elif card_value == 11:
        card_type = 'A'
    else:
        card_type = str(card_value)
    return card_value, card_type


def player_turn():
    hand = []
    hand_type = []
    value, card = take_card()
    hand.append(value)
    hand_type.append(card)
    card_add = 'y'
    while (card_add.lower()[0] == "y"):
        value, card = take_card()
        hand.append(value)
        hand_type.append(card)
        hand = ace_changer(hand)
        print("Your hand: {}, score: {}".format(list_to_string(hand_type),
              sum(hand)))
        if (check_21(hand)) or (check_bj(hand)):
            break
        card_add = input("Do you want take a card? (y/n) ")
        print('=' * 10)
    return hand, list_to_string(hand_type)


def dealer_turn():
    hand = []
    hand_type = []
    while sum(hand) < 17:
        value, card = take_card()
        hand.append(value)
        hand_type.append(card)
        hand = ace_changer(hand)
    return hand, list_to_string(hand_type)


def result_of_round(name, player_hand, player_hand_type,
                    dealer_hand, dealer_hand_type):
    print('=' * 10)
    print("Done! Let's check: ")
    print('{} has: {} score = {}'.format(name, player_hand_type,
          sum(player_hand)))    
    print('Dealer has: {} score = {}'.format(dealer_hand_type,
          sum(dealer_hand)))
    return None


def result_of_game(name, player_win, dealer_win):
    print('The Final after {} games:'.format(player_win + dealer_win))
    print('{}: {} | Dealer: {}'.format(name, player_win, dealer_win))
    return None
  
  
def main():
    player_win, dealer_win = game_loop(name)
    result_of_game(name, player_win, dealer_win)


if __name__ == "__main__": main()
