def draw_lines(tab):
    """
    Function draws all the lines need for tic tac toe game in a given game board
    :param tab:
    :return tab:
    """
    tab[0][1] = ' | '
    tab[0][3] = ' | '
    tab[1][0] = ' - '
    tab[1][1] = ' + '
    tab[1][2] = ' - '
    tab[1][3] = ' + '
    tab[1][4] = ' - '
    tab[2][1] = ' | '
    tab[2][3] = ' | '
    tab[3][0] = ' - '
    tab[3][1] = ' + '
    tab[3][2] = ' - '
    tab[3][3] = ' + '
    tab[3][4] = ' - '
    tab[4][1] = ' | '
    tab[4][3] = ' | '
    return tab


def print_board(tab):
    """
    Function prints the game board on terminal screen
    :param tab:
    :return:
    """
    for i in range(0, 5):
        for a in range(0, 5):
            print(tab[i][a], end='')
        print("")


def mark_x(tab, place):
    """
    Function mark a player x move in a given place
    :param tab:
    :param place:
    :return:
    """
    if place < 4:
        if place == 1:
            tab[0][0] = ' X '
        if place == 2:
            tab[0][2] = ' X '
        if place == 3:
            tab[0][4] = ' X '
    elif place < 7:
        if place == 4:
            tab[2][0] = ' X '
        if place == 5:
            tab[2][2] = ' X '
        if place == 6:
            tab[2][4] = ' X '
    else:
        if place == 7:
            tab[4][0] = ' X '
        if place == 8:
            tab[4][2] = ' X '
        if place == 9:
            tab[4][4] = ' X '
    return tab


def mark_o(tab, place):
    """
        Function mark a player o move in a given place
        :param tab:
        :param place:
        :return:
        """
    if place < 4:
        if place == 1:
            tab[0][0] = ' O '
        if place == 2:
            tab[0][2] = ' O '
        if place == 3:
            tab[0][4] = ' O '
    elif place < 7:
        if place == 4:
            tab[2][0] = ' O '
        if place == 5:
            tab[2][2] = ' O '
        if place == 6:
            tab[2][4] = ' O '
    else:
        if place == 7:
            tab[4][0] = ' O '
        if place == 8:
            tab[4][2] = ' O '
        if place == 9:
            tab[4][4] = ' O '
    return tab


def win_check(tab):
    """
    Function checks if any of two player has a marks sequence that makes them a winner
    :param tab:
    :return:
    """
    if tab[0][0] == ' X ':
        if tab[0][2] == ' X ' and tab[0][4] == ' X ':
            return 1
        if tab[2][0] == ' X ' and tab[4][0] == ' X ':
            return 1

    if tab[2][2] == ' X ':
        if tab[0][2] == ' X ' and tab[4][2] == ' X ':
            return 1
        if tab[2][0] == ' X ' and tab[2][4] == ' X ':
            return 1
        if tab[0][0] == ' X ' and tab[4][4] == ' X ':
            return 1
        if tab[4][0] == ' X ' and tab[0][4] == ' X ':
            return 1

    if tab[4][4] == ' X ':
        if tab[2][4] == ' X ' and tab[0][4] == ' X ':
            return 1
        if tab[4][0] == ' X ' and tab[4][2] == ' X ':
            return 1

    if tab[0][0] == ' O ':
        if tab[0][2] == ' O ' and tab[0][4] == ' O ':
            return 2
        if tab[2][0] == ' O ' and tab[4][0] == ' O ':
            return 2

    if tab[2][2] == ' O ':
        if tab[0][2] == ' O ' and tab[4][2] == ' O ':
            return 2
        if tab[2][0] == ' O ' and tab[2][4] == ' O ':
            return 2
        if tab[0][0] == ' O ' and tab[4][4] == ' O ':
            return 2
        if tab[4][0] == ' O ' and tab[0][4] == ' O ':
            return 2

    if tab[4][4] == ' O ':
        if tab[2][4] == ' O ' and tab[0][4] == ' O ':
            return 2
        if tab[4][0] == ' O ' and tab[4][2] == ' O ':
            return 2

    return 0


def place_check(tab, place):
    if place < 4:
        if place == 1 and (tab[0][0] == ' X ' or tab[0][0] == ' O '):
            return 0
        if place == 2 and (tab[0][2] == ' X ' or tab[0][2] == ' O '):
            return 0
        if place == 3 and (tab[0][4] == ' X ' or tab[0][4] == ' O '):
            return 0
    elif place < 7:
        if place == 4 and (tab[2][0] == ' X ' or tab[2][0] == ' O '):
            return 0
        if place == 5 and (tab[2][2] == ' X ' or tab[2][2] == ' O '):
            return 0
        if place == 6 and (tab[2][4] == ' X ' or tab[2][4] == ' O '):
            return 0
    else:
        if place == 7 and (tab[4][0] == ' X ' or tab[4][0] == ' O '):
            return 0
        if place == 8 and (tab[4][2] == ' X ' or tab[4][2] == ' O '):
            return 0
        if place == 9 and (tab[4][4] == ' X ' or tab[4][4] == ' O '):
            return 0
    return 1


print('Welcome to TIC TAC TOE')
print('Please set names for the players (Player 1 starts as X):')
print('Player 1: ', end='')
player_1 = input()
print('Player 2: ', end='')
player_2 = input()

print('Take a look at the board controls layout')
print(' 1  |  2  |  3  \n -  +  -  +  -  \n 4  |  5  |  6  \n -  +  -  +  - \n 7  |  8  |  9  ')

answer = 'n'
counter = 0
while answer != 'y':
    if counter > 10:
        print('I see you won\'t ever be ready')
        quit()
    print('Are you ready to begin the fight? (y or n): ', end='')
    answer = input()
    counter += 1

w, h = 5, 5
board = [['   ' for x in range(w)] for y in range(h)]
board = draw_lines(board)

win = 0    # zmienna oznaczaja ktory gracz wygral
move = 1   # zmienna oznaczajaca ktory gracz wykonuje nastepny ruch
mark = 0   # zmienna temporary dla zapisu ruchu gracza
first = 0  # dwie zmienne ilosci wykonanych ruchow, gra nie sprawdza wygranej ponizej 3 ruchow jednej ze stron
second = 0

while win == 0:
    print_board(board)

    if move == 1:
        print('It\'s time for {}\'s move, chose wisely: '.format(player_1), end='')
        mark = input()
        mark = int(mark)

        while place_check(board, mark) != 1:
            print('Not a Valid move, this place is already taken!')
            print('Try again: ', end='')
            mark = input()
            mark = int(mark)

        board = mark_x(board, mark)
        first += 1
        move = 2
    elif move == 2:
        print('It\'s time for {}\'s move, chose wisely: '.format(player_2), end='')
        mark = input()
        mark = int(mark)

        while place_check(board, mark) != 1:
            print('Not a Valid move, this place is already taken!')
            print('Try again: ', end='')
            mark = input()
            mark = int(mark)

        board = mark_o(board, mark)
        second += 1
        move = 1

    if first > 2 or second > 2:
        if win_check(board) == 1:
            win = 1
        elif win_check(board) == 2:
            win = 2

    if first + second == 9:
        break


print_board(board)
print('Game over')
if win == 0:
    print('Oh it\'s a draw!')
if win == 1:
    print('{} wins this session'.format(player_1))
if win == 2:
    print('{} wins this session'.format(player_2))
