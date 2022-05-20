from random import randint


# Print the actual amount of rocks
def actual_rocks(comp_rocks, player_rocks, player_name):
    print(f'Computer has {comp_rocks} rocks')
    print(f'{player_name} has {player_rocks} rocks')


# Check user's enter is correct
def check_enter(min_value, max_value):
    isWrong = True
    while isWrong:
        try:
            guess = int(input())
            if min_value <= guess <= max_value:
                isWrong = False
            else:
                print(
                    f'Expected integer from {min_value} to {max_value}, got {guess}.')
        except:
            print('It\'s not an integer.')
    return guess


# Computer's turn
def comp_turn(comp_rocks, player_rocks, player_name):
    comp_bet = randint(1, comp_rocks)
    print('Computer made a bet. Please make your bet:')
    player_bet = check_enter(1, player_rocks)
    comp_guess = randint(0, 1)
    if comp_guess:
        print(
            f'Computer guessed your bet had an odd amount of rocks. It bet {comp_bet} rocks.')
    else:
        print(
            f'Computer guessed your bet had an even amount of rocks. It bet {comp_bet} rocks.')
    winner = 'comp' if comp_guess == player_bet % 2 else 'player'
    comp_rocks, player_rocks = rocks_calc(comp_rocks, player_rocks, comp_bet,
                                          player_bet, winner)
    curr_turn = player_name
    return comp_rocks, player_rocks, curr_turn


# Player's turn
def player_turn(comp_rocks, player_rocks):
    print('Please make your bet:')
    player_bet = check_enter(1, player_rocks)
    comp_bet = randint(1, comp_rocks)
    print('Computer made a bet. Guess is it even (type 0) or odd (type 1):')
    player_guess = check_enter(0, 1)
    if player_guess:
        print(
            f'You guessed computer\'s bet had an odd amount of rocks while it had {comp_bet} rocks.')
    else:
        print(
            f'You guessed computer\'s bet had an even amount of rocks while it had {comp_bet} rocks.')
    winner = 'player' if player_guess == comp_bet % 2 else 'comp'
    comp_rocks, player_rocks = rocks_calc(comp_rocks, player_rocks, comp_bet,
                                          player_bet, winner)
    curr_turn = 'Computer'
    return comp_rocks, player_rocks, curr_turn


# Calculate the amount of rocks after the game round
def rocks_calc(comp_rocks, player_rocks, comp_bet, player_bet, winner):
    if winner == 'comp':
        print('Computer wins! \n')
        comp_rocks += comp_bet
        player_rocks -= comp_bet
    else:
        print('You win! \n')
        comp_rocks -= player_bet
        player_rocks += player_bet
    comp_rocks, player_rocks = negative_check(comp_rocks, player_rocks)
    return comp_rocks, player_rocks


# Check the score isn't negative
def negative_check(comp_rocks, player_rocks):
    if comp_rocks < 0:
        comp_rocks, player_rocks = 0, 20
    if player_rocks < 0:
        comp_rocks, player_rocks = 20, 0
    return comp_rocks, player_rocks


def main():
    print('Do you remember \'Squid game\'? Let\'s play Gganbu!')

    # Check that player's name isn't 'Computer'
    isWrong = True
    while isWrong:
        player_name = input('Please enter your name: ')
        if player_name == 'Computer':
            print(
                'You can\'t use this name. It\'s Computer\'s name :) Don\'t confuse them!')
        else:
            isWrong = False
    print('Nice! I like it!\n')

    # Determine who plays first
    turn_bet = randint(1, 2)
    print(
        'Who starts the game? Guess what integer from 1 to 2 was chosen by computer:')
    curr_turn = player_name if check_enter(1, 2) == turn_bet else 'Computer'
    print(f'Computer guessed {turn_bet}. {curr_turn} starts the game.\n')

    # Set initial amount of rocks
    comp_rocks = player_rocks = 10

    # Game loop
    while comp_rocks > 0 and player_rocks > 0:

        # Print actual amount of rocks
        actual_rocks(comp_rocks, player_rocks, player_name)

        # Make a bet
        print(f'It\'s {curr_turn}\'s turn')
        if curr_turn == 'Computer':
            comp_rocks, player_rocks, curr_turn = comp_turn(comp_rocks,
                                                            player_rocks,
                                                            player_name)
        else:
            comp_rocks, player_rocks, curr_turn = player_turn(comp_rocks,
                                                              player_rocks)

    # Printing result of the game
    print('The game is over!')
    actual_rocks(comp_rocks, player_rocks, player_name)
    winner = player_name if comp_rocks == 0 else 'Computer'
    print(f'{winner} wins!')


if __name__ == "__main__":
    main()
