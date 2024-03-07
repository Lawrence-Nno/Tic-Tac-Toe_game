import random


def print_card(card):
    for row in card:
        print(row)


def place_card(position, char):
    if position in position_left:
        if position == 1:
            t_list[0][0] = char
        elif position == 2:
            t_list[0][1] = char
        elif position == 3:
            t_list[0][2] = char
        elif position == 4:
            t_list[1][0] = char
        elif position == 5:
            t_list[1][1] = char
        elif position == 6:
            t_list[1][2] = char
        elif position == 7:
            t_list[2][0] = char
        elif position == 8:
            t_list[2][1] = char
        elif position == 9:
            t_list[2][2] = char
        else:
            print("Enter a valid position")
    else:
        print("That position is already occupied")


def check_result():
    if t_list[0][0] == t_list[0][1] == t_list[0][2] == 'X':
        print("You won")
        return False
    elif t_list[0][0] == t_list[0][1] == t_list[0][2] == 'O':
        print("You lost")
        return False
    if t_list[1][0] == t_list[1][1] == t_list[1][2] == 'X':
        print("You won")
        return False
    elif t_list[1][0] == t_list[1][1] == t_list[1][2] == 'O':
        print("You lost")
        return False
    if t_list[2][0] == t_list[2][1] == t_list[2][2] == 'X':
        print("You won")
        return False
    elif t_list[2][0] == t_list[2][1] == t_list[2][2] == 'O':
        print("You lost")
        return False
    if t_list[0][0] == t_list[1][0] == t_list[2][0] == 'X':
        print("You won")
        return False
    elif t_list[0][0] == t_list[1][0] == t_list[2][0] == 'O':
        print("You lost")
        return False
    if t_list[0][1] == t_list[1][1] == t_list[2][1] == 'X':
        print("You won")
        return False
    elif t_list[0][1] == t_list[1][1] == t_list[2][1] == 'O':
        print("You lost")
        return False
    if t_list[0][2] == t_list[1][2] == t_list[2][2] == 'X':
        print("You won")
        return False
    elif t_list[0][2] == t_list[1][2] == t_list[2][2] == 'O':
        print("You lost")
        return False
    if t_list[0][0] == t_list[1][1] == t_list[2][2] == 'X':
        print("You won")
        return False
    elif t_list[0][0] == t_list[1][1] == t_list[2][2] == 'O':
        print("You lost")
        return False
    if t_list[0][2] == t_list[1][1] == t_list[2][0] == 'X':
        print("You won")
        return False
    elif t_list[0][2] == t_list[1][1] == t_list[2][0] == 'O':
        print("You lost")
        return False
    else:
        return True


game = True
while game:
    t_list = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    position_list = []
    position_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Welcome to the TIC TAC TOE Game\nYour character is 'X', while computer is 'O'")
    print_card(t_list)

    def play_game():
        print(f"You have {len(position_left)} possible positions and they are\n{position_left}")
        while True:
            try:
                entry = int(input("Enter a Position: "))
            except ValueError:
                print("Enter a valid position")
            else:
                break

        place_card(entry, 'X')
        position_left.remove(entry)
        print_card(t_list)
        if check_result():
            if len(position_left) > 0:
                comp_position = random.choice(position_left)
                place_card(comp_position, 'O')
                position_left.remove(comp_position)
                print("Computer's turn..")
                print_card(t_list)
                if check_result():
                    play_game()
            else:
                print("It's a draw")

    play_game()
    play_on = input("if you wish to continue type 'y': ")
    if play_on.lower() == 'y':
        pass
    else:
        game = False
