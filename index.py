# Function to display the board
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# Function to take player input
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to input X or O? ').upper()

    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

# player_input()

#Function to place the 'X' or 'O' marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)
