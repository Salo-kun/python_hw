# def game_loop(name):
#     player_win = 0
#     dealer_win = 0
#     play_again = 'yes'
#     while play_again.lower[0] == 'y':
#         player_hand, player_hand_type = player_turn()
#         dealer_hand, dealer_hand_type = dealer_turn()
#         player_score, dealer_score = game_construct(player_hand, dealer_hand)
#         result_of_round(name, player_hand, player_hand_type, dealer_hand, dealer_hand_type)
#         if player_score > dealer_score:
#             print('{} win!'.format(name))
#             player_win += 1
#         else:
#             print('Dealer win!')
#             dealer_win += 1
#         play_again = input('Do you want to continue (Y or N)? ')
#     return player_win, dealer_win


play_again = 'yes'
while play_again.lower()[0] == 'y':
    play_again = input('Do you want to continue (Y or N)? ')
    play_again