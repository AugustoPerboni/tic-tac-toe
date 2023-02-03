import time
from random import randint
from multiplayer import print_game_table, game_status

def winner_or_block_spot(game_matrix: list) -> list: # Return the desire position in positive case and in negative return 0
    ''' First check if there is any position needed to be fill in order to win the game and then chechk ir there is any position that could block the user'''
    # Check the main diagonal
    main_diagonal = []
    main_diagonal.append(game_matrix[0][0])
    main_diagonal.append(game_matrix[1][1])
    main_diagonal.append(game_matrix[2][2])
    if main_diagonal.count('O') == 2:
        for i in range(3):
            if main_diagonal[i] == '':
                main_diagonal_entry =[i,i]
                return main_diagonal_entry
    # Check secondary diagonal
    secondary_diagonal = []
    secondary_diagonal.append(game_matrix[0][2])
    secondary_diagonal.append(game_matrix[1][1])
    secondary_diagonal.append(game_matrix[2][0])
    if secondary_diagonal.count('O') == 2:
        if secondary_diagonal[0] == '':
            return [0,2]
        elif secondary_diagonal[1] == '':
            return [1,1]
        elif secondary_diagonal[2] == '':
            return [2,0]
    # Check if some line miss one element to win
    for i in range(3):
        if game_matrix[i].count('O') == 2:
            for j in range(3):
                if game_matrix[i][j] == '':
                    block_spot = [i,j]
                    return block_spot

    # Tranpose de matrix
    game_matrix = [[row[i] for row in game_matrix] for i in range(len(game_matrix))]

    # Do the same for the lines of the transposed matrix, the same of the collumns of the original matrix
    for i in range(3):
        if game_matrix[i].count('O') == 2:
            for j in range(3):
                if game_matrix[i][j] == '':
                    # We need to return the values changed once we are working with the transposed matrix
                    block_spot = [j,i]
                    return block_spot


    # Locking for spot to block the user
    #  REMEMBER the matrix is transposed
    # Check if some line miss one element to block
    for i in range(3):
        if game_matrix[i].count('X') == 2:
            for j in range(3):
                if game_matrix[i][j] == '':
                    block_spot = [j,i]
                    return block_spot
    # Tranpose de matrix
    game_matrix = [[row[i] for row in game_matrix] for i in range(len(game_matrix))]
    # Check the main diagonal 
    main_diagonal = []
    main_diagonal.append(game_matrix[0][0])
    main_diagonal.append(game_matrix[1][1])
    main_diagonal.append(game_matrix[2][2])
    if main_diagonal.count('X') == 2:
        for i in range(3):
            if main_diagonal[i] == '':
                main_diagonal_entry =[i,i]
                return main_diagonal_entry
    # Check secondary diagonal
    secondary_diagonal = []
    secondary_diagonal.append(game_matrix[0][2])
    secondary_diagonal.append(game_matrix[1][1])
    secondary_diagonal.append(game_matrix[2][0])
    if secondary_diagonal.count('X') == 2:
        if secondary_diagonal[0] == '':
            return [0,2]
        elif secondary_diagonal[1] == '':
            return [1,1]
        elif secondary_diagonal[2] == '': 
            return [2,0]

    # Do the same for the lines of the transposed matrix, the same of the collumns of the original matrix
    for i in range(3):
        if game_matrix[i].count('X') == 2:
            for j in range(3):
                if game_matrix[i][j] == '':
                    # We need to return the values changed once we are working with the transposed matrix
                    block_spot = [i,j]
                    return block_spot
    return 0

def single_player_intro() -> None:
    print('Welcome to tic-tac-toe, single player. In this game you will have the change to beat me (programm) in tic-tac-toe. You will start, please choose the position that you want to mark in using the following pattern:[line] [collumn], both going from 0 to 2:\n Let\'s begging:\n')
    
def pick_side(game_matrix: list, used_positions = [4]) -> list:
    ''' Pick one random side given the game matrix'''
    # consider the following matrix positions
    #|--0--|
    #|1---2|
    #|--3--|

    randit_not_used = randint(0,3)
    while randit_not_used in used_positions:
        randit_not_used = randint(0,3)

    match randint(0,3):
        case 0:
            ans = [0,1]
        case 1:
            ans = [1,0]
        case 2:
            ans = [1,2]
        case 3:
            ans = [2,1]

    if game_matrix[ans[0]][ans[1]] != '':
        used_positions.append([ans[0],ans[1]])
        ans = pick_side(game_matrix, used_positions)
    return ans
       
def pick_rand(game_matrix: list, used_positions = [[4,4]]) -> list:
    ''' Pick one random spot given the game matrix'''

    # consider the following matrix positions
    #|1 2 3|
    #|4 5 6|
    #|7 8 9|

    not_used_row = randint(0,2)
    not_used_column = randint(0,2)
    while [not_used_row, not_used_column] in used_positions:
        not_used_row = randint(0,2)
        not_used_column = randint(0,2)

    if game_matrix[not_used_row][not_used_column] != '':
        used_positions.append([not_used_row,not_used_column])
        [not_used_row,not_used_column] = pick_rand(game_matrix, used_positions)
    return [not_used_row,not_used_column]

def game_intro_single_player() -> list:
    ''' Introduce the game to the players'''
    game_rules = ("1. The game is played on a grid that's 3 squares by 3 squares. \n2. You are X, i am 0. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie. ")

    player = []
    print('Welcome to tic-tac-toe! \n', end ='')
    print('Do you know that game rules? (Yes or No)',end = '  ')
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

i = 1
user_moves = [''] # Keep history of the user movements

game_matrix = [['','',''],['','',''],['','','']] 
game_intro_single_player()
print_game_table(game_matrix)
while True:   
    # The following code will be responsable to read and plot the user option
    print('Your turn, choose your position:', end='')
    user_selection = list(input())
    selected_row = int(user_selection[0])
    selected_column = int(user_selection[2])
    # Validate the input
    if ((selected_column >2 or selected_row >2) or game_matrix[selected_row][selected_column] == 'X' or game_matrix[selected_row][selected_column] == 'O') or len(user_selection) != 3 :
                print('Position already choosen, input out of range or invalid inputs.\nPlease try again')
                continue
    game_matrix[selected_row][selected_column] = 'X'
    print_game_table(game_matrix)
    if game_status(game_matrix) == 1:
        print('Congratulations you won')
        quit()

    if i == 9:
        print('The game tied, do you wanna play again? (Yes/No)')
        match input():
            case 'Yes':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case 'YES':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case 'yes':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case 'Y':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case 'y':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case '':
                i = 1
                game_matrix = [['','',''],['','',''],['','','']]
                user_moves = ['']
                print_game_table(game_matrix)
                continue
            case _:
                quit()
       
    i = i +1
    
    # The following code is responsable to analyse the choosen position and choose how to respond to it
    
    # The element add to user_moves is a tuple in order to facilitate the use in match statements
    user_moves.append((selected_row,selected_column)) 
    if i == 2:
        # If corner -> middle
        match user_moves[1]:
            case (0,0):
                next_move = [1,1]
            case (0,2):
                next_move = [1,1]
            case (2,0):
                next_move = [1,1]
            case (2,2):
                next_move = [1,1]
            case _: 
                next_move = pick_rand(game_matrix)

        game_matrix[next_move[0]][next_move[1]] = 'O'
        print('My turn:')
        time.sleep(0.5)
        print_game_table(game_matrix)
    
    elif i == 4:

        match user_moves[2]:
            case (0,0) if user_moves[1] == (2,2):
                next_move = pick_side(game_matrix)
            case (0,2) if user_moves[1] == (2,0):
                next_move = pick_side(game_matrix)
            case (2,0) if user_moves[1] == (0,2):
                next_move = pick_side(game_matrix)
            case (2,2) if user_moves[1] == (0,0):
                next_move = pick_side(game_matrix)
            case _:
                if winner_or_block_spot(game_matrix) != 0:
                    next_move = winner_or_block_spot(game_matrix)
                else:
                    next_move = pick_rand(game_matrix)
        game_matrix[next_move[0]][next_move[1]] = 'O'
        print('My turn:')
        time.sleep(0.5)
        print_game_table(game_matrix)

        
    else:
        win_or_block = winner_or_block_spot(game_matrix)
        if win_or_block != 0:
            next_move = win_or_block
        else:
            next_move = pick_rand(game_matrix)

        game_matrix[next_move[0]][next_move[1]] = 'O'
        print('My turn:')
        time.sleep(0.5)
        print_game_table(game_matrix)
        if game_status(game_matrix) == 1:
            print('You lose, more lucky next time')
            quit()
    
        
    i = i + 1



