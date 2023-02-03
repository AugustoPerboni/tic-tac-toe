def print_standart_line() -> None:
    ''' prints a regular horizontal line just used to form the shape of the game in command line'''

    print( (2 * ( (7 * ' ') + ('|'))) )

def print_game_line(line_number: int, game_matrix: list) -> None:
    ''' prints the line with game status informations'''

    first_value  = game_matrix[line_number][0].center(7)
    second_value = game_matrix[line_number][1].center(7)
    third_value  = game_matrix[line_number][2].center(7)
    print(f'{first_value}|{second_value}|{third_value}')

def print_intersection_line() -> None:
    ''' print a horizontal line that is the instersectio of two standart lines'''
    print( (2 * (7 * '―' + '+') + 7*'―') )

def print_game_table(game_matrix: list) -> None:
    ''' print the game table with the data from the game matrix'''
    for i in range (3):
        print_standart_line()
        print_game_line(i,game_matrix)
        print_standart_line()
        if i != 2:
            print_intersection_line()
    print('\n')
    
def game_intro() -> list:
    ''' Introduce the game to the players'''
    game_rules = ("1. The game is played on a grid that's 3 squares by 3 squares. \n2. You are X, your friend is O. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. ")

    player = []
    print('Welcome to tic-tac-toe! \nFirst Player:', end ='')
    player.append(input()) 
    print('Second Player:', end = '')
    player.append(input())
    print('Do you know that game rules? (Yes or No)')
    match input():
        case 'Yes':
            pass
        case 'YES':
            pass
        case 'yes':
            pass
        case 'Y':
            pass
        case 'y':
            pass
        case _:
            print(game_rules)
    print('\n\nLet\'s start the game. \nTo choose a spot you just need to select the line and column that you want to pin.\nFor exemple: 0 0, would put a pin in the first element of the main diagonal\n\n\n')
    return player

def game_status(game_matrix:list) -> int:
    ''' Chechk if someone won the game'''

    # Return 1 if there is a winning pattern
    # Analysing the main diagonal
    if (game_matrix[0][0]==game_matrix[1][1]==game_matrix[2][2] or game_matrix[0][2] == game_matrix[1][1]==game_matrix[2][0]) & (game_matrix[1][1] != ''):
        return 1

    # Analysing the rows
    if 1 == ((game_matrix.count(['X','X','X'])) or (game_matrix.count(['O','O','O'])) ):
        return 1
    
    # To analyse the columns lets transpose the matrix and analyse the rows of the transposed matrix
    game_matrix = [[row[i] for row in game_matrix] for i in range(len(game_matrix))]

    if 1 == ((game_matrix.count(['X','X','X'])) or (game_matrix.count(['O','O','O'])) ):
        return 1
    
# This conditions make the module a script when executed with __name__ = __main__    
if __name__ == '__main__':
    game_matrix = [['','',''],['','',''],['','','']]
    player = game_intro()

    print_game_table(game_matrix)
    i = 0
    while True:
        i = i + 1 
        if i == 10:
            print('The game is tied, there is no winner.\nTo play another game type \'new game\': ')
            if input() == 'new game':
                i = 0
                game_matrix = [['','',''],['','',''],['','','']]
                continue
        if i % 2 != 0: 
            print(f'Turn {i} of {player[0]}:',end='')
            player_selection = list(input())
            selected_row = int(player_selection[0])
            selected_column = int(player_selection[2])
            # Check if the choosen spot is valid
            if ((selected_column > 2 or selected_row > 2) or game_matrix[selected_row][selected_column] == 'X' or game_matrix[selected_row][selected_column] == 'O'):
                print('Position already choosen, or input out of range.\nPlease try again')
                i = i -1
                continue
            game_matrix[selected_row][selected_column] = 'X'
            # Check if the game is finished 
            if game_status(game_matrix) == 1:
                print(f'\n\n\n{player[0]} won the game')
                print('Final game table:')
                print_game_table(game_matrix)
                quit()
        else:
            print(f'Turn {i} of {player[1]}:',end='')
            player_selection = list(input())
            selected_row, selected_column = int(player_selection[0]), int(player_selection[2])
            if ((selected_column >2 or selected_row >2) or game_matrix[selected_row][selected_column] == 'X' or game_matrix[selected_row][selected_column] == 'O'):
                print('Position already choosen, or input out of range.\nPlease try again')
                i = i -1
                continue
            game_matrix[selected_row][selected_column] = 'O'
            if game_status(game_matrix) == 1:
                print(f'\n\n\n{player[1]} won the game')
                print('Final game table:')
                print_game_table(game_matrix)
                quit()    
        print_game_table(game_matrix)