import random

board = [" " for i in range(10)]
empty = ' '

def drawBoard(board):
    print("    |    |")
    print("  " + board[1] + " | " + board[2] + "  | " + board[3])
    print("    |    |")
    print("  ----------")
    print("    |    |")
    print("  " + board[4] + " | " + board[5] + "  | " + board[6])
    print("    |    |")
    print("  ----------")
    print("    |    |")
    print("  " + board[7] + " | " + board[8] + "  | " + board[9])
    print("    |    |")

def player():
    place = int(input('1-9: '))
    board[place] = 'X'
    return place

def comp(player):
    pass

def boardIsEmpty():
    pass

def main():
    comp(player())
    drawBoard(board)

if __name__ == '__main__':
    main()