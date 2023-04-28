first_user = input("Enter first player's name >>> ")  # First player's name
second_user = input("Enter second player's name  >>> ")  # Second player's name

p = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}  # Dictionary with positions
pos_lst = []  # Game elements position list


def x_pos(pos):
    if pos in pos_lst:  # Checks if X position is occupied
        while True:
            new_pos = input("This position is occupied, please enter another! >>> ")
            if new_pos not in pos_lst:
                p[int(new_pos)] = 'X'
                pos_lst.append(new_pos)
                break

    for i in range(1, 10):  # Appends X positions with is not occupied to pos_lst
        if pos == p[i]:
            p[i] = 'X'
            pos_lst.append(pos)


def o_pos(pos):
    if pos in pos_lst:  # Checks if O position is occupied
        while True:
            new_pos = input("This position is occupied, please enter another! >>> ")
            if new_pos not in pos_lst:
                p[int(new_pos)] = 'O'
                pos_lst.append(new_pos)
                break

    for i in range(1, 10):  # Appends O positions with is not occupied to pos_lst
        if pos == p[i]:
            p[i] = 'O'
            pos_lst.append(pos)


def draw():  # Checks if it's draw
    word = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]  # Creates word with game elements
    if word.count("X") == 5 or word.count("O") == 5:
        return True


def rematch(answer):  # Rematch function
    if answer == 'y' or answer == 'yes':  # Checks if players want to play again
        return True


def table_cleaner():  # Game area reset
    pos_lst.clear()
    for i in range(1, len(p) + 1):
        p[i] = str(i)


def table_print():  # Game area
    print(f'''{p[1]} | {p[2]} | {p[3]}
{p[4]} | {p[5]} | {p[6]}
{p[7]} | {p[8]} | {p[9]}''')


def win():  # Win function
    if p[1] == p[4] == p[7] or p[1] == p[2] == p[3] or p[1] == p[5] == p[9] or p[3] == p[5] == p[7] or p[2] == \
            p[5] == p[8] or p[4] == p[5] == p[6] or p[7] == p[8] == p[9] or p[3] == p[6] == p[9]:
        return True


def input_validator(user_name, sign):  # Input validator
    player_input = input(f"{user_name}, enter '{sign}' position  >>> ")
    if len(player_input) > 1 or player_input.isalpha():
        while True:
            player_input = input(f"{user_name}, enter '{sign}' valid position  >>> ")
            if len(player_input) == 1 and player_input.isnumeric():
                break
    return player_input


def tic_tac_toe_game():  # Game
    while True:
        table_print()  # Prints game area
        player_1 = input_validator(first_user, 'X')  # Player_1 input
        x_pos(player_1)  # X position func
        if win():  # Checks if someone won
            table_print()  # Prints game area
            print(f'{first_user}, you won this game!!!☺ ')
            answer = input("Do you want play again?[y/n] >>>")
            if rematch(answer):  # Checks if players want to play again
                table_cleaner()
            else:
                break
        table_print()  # Prints game area
        if draw():  # Checks if it's draw
            print("It's draw! ☺ ")
            answer = input("Do you want to play again?[y/n] >>>")
            if rematch(answer):  # Checks if players want to play again
                table_cleaner()
                table_print()
            else:
                break
        player_2 = input_validator(second_user, 'O')  # Player_2 input
        o_pos(player_2)  # O position func
        if win():  # Checks if someone won
            table_print()  # Prints game area
            print(f'{second_user}, you won this game!!!☺ ')
            answer = input("Do you want to play again?[y/n] >>>")
            if rematch(answer):  # Checks if players want to play again
                table_cleaner()
            else:
                break
        if draw():  # Checks if players want to play again
            table_print()  # Prints game area
            print("It's draw! ☺ ")
            answer = input("Do you want to play again?[y/n] >>>")
            if rematch(answer):  # Checks if players want to play again
                table_cleaner()
            else:
                break


tic_tac_toe_game()
