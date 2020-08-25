# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 
# to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or 
# False depending on if the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, 
# at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
# The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
# This function should detect when a bug has resulted in an improper chess board.

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '3a': 'gdog',  '9z': 'wrook'}
legalColors = ['w','b']
legalPieces = ['king','queen','rook','bishop','knight','pawn']
legalPositions = {
    'letter':['a','b','c','d','e','f','g','h'],
    'number':[1,2,3,4,5,6,7,8]
    }

def isValidChessBoard():
    bKing = 0
    wKing = 0
    bPiece = 0
    wPiece = 0
    isValid = True

    for n in chessBoard:
        if bKing + wKing > 2:
            isValid = False
        elif bPiece + wPiece > 32:
            isValid = False

        if chessBoard[n] == 'bking':
            bKing = bKing + 1
        elif chessBoard[n] == 'wking':
            wKing = wKing + 1
        
        if chessBoard[n][1:] in legalPieces:
            if chessBoard[n][0] == 'b':
                bPiece = bPiece + 1
            elif chessBoard[n][0] == 'w':
                wPiece = wPiece + 1
        elif chessBoard[n] == '':
            None
        else:
            print(chessBoard[n] + ' is not a legal piece')
            isValid = False

        if n[1] in legalPositions['letter']:
            if n[0] in str(legalPositions['number']):
               None
            else:
                isValid = False
                print(n + " is not a legal space")
            None
        else:
            isValid = False
            print(n + " is not a legal space")

    print(str(bKing + wKing) + ' kings')
    print(str(bPiece) + ' black pieces')
    print(str(wPiece) + ' white pieces')
    if isValid == True:
        print('The board is Valid')    
    else:
        print('The board is NOT Valid')

isValidChessBoard()