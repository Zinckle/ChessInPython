
from graphics import *

class Piece:
    colour = "" ##b for black, w for white
    title = ""  ## Pawn, King, Queen, Rook, Bishop, kNight
    image = "" #assign the image for the respective piece
    xpos = "" ##position in the x axis
    ypos = "" ##position in the y axis
    pieceImage = ""

    def __init__(self, c, t, i, x, y, p):
        self.colour = c   
        self.title = t
        self.image = i
        self.xpos = x
        self.ypos = y
        self.pieceImage = p

    def setX(self, x):
        self.xpos = x   

    def setX(self, y):
        self.ypos = y   

    def copy(self):

        return Piece(self.colour, self.title, self.image, self.xpos, self.ypos, self.pieceImage)

class Square:
    colour = "" ## black or white square
    topxpos = "" ##position in the x axis
    topypos = "" ##position in the y axis
    botxpos = "" ##position in the x axis
    botypos = "" ##position in the y axis

    xpos = "" ##position in the x axis
    ypos = "" ##position in the y axis

    currentPiece = ""##what peice is in this position

    def __init__(self, c, tx, ty, bx, by):
        self.colour = c   
        self.topxpos = tx
        self.topypos = ty
        self.botxpos = bx
        self.botypos = by    
        self.xpos = bx-50
        self.ypos = by-50
        ##self.currentPiece = p
    
    def getColour(self):

        return self.colour

    def getClicked(self, click):

        return (((click.getX() < self.botxpos) and (click.getX() >= self.topxpos)) and ((click.getY() < self.botypos) and (click.getY() >= self.topypos)))

def buildBoard(win, board):
    for i in range(8):
        if (i % 2 != 0):
            q = 1
        else:
            q = 0
        
        for j in range(8):
            rect = Rectangle(Point(0+(100*(i)), 0+(100*j)), Point(100+(100*(i)), 100+(100*j)))
            
            rect.draw(win)
            if ((j+q) % 2 == 0):
                rect.setFill('White')
                board[i][j] = Square("white",0+(100*i), 0+(100*j), 100+(100*i), 100+(100*j))
            else:
                rect.setFill('dark grey')
                board[i][j] = Square("dark grey",0+(100*i), 0+(100*j), 100+(100*i), 100+(100*j))
    return board

def pawnCheck(board, x1, y1, x2, y2):
    #TODO: implement en passant
    #TODO: implement the pawn changing into a selected peice when it reaches the back file
    
    pawn = board[x1][y1].currentPiece
    if (pawn.colour == "w"):
        indicator = -1
        inital = 6
        if (y1<y2):
            return False
    elif (pawn.colour == "b"): 
        indicator = 1
        inital = 1
        if (y1>y2):
            return False

    if((y1 == inital) and (y2 == y1+indicator*2) and (x1 == x2) and (board[x1][y1+indicator].currentPiece == "") and (board[x2][y2].currentPiece == "")):
        print("1")
        return True

    elif((y2 == y1+indicator) and (x1 == x2) and (board[x2][y2].currentPiece == "")):
        print("2")
        return True

    try:
        if((board[x1+1][y1+indicator].currentPiece != "") and (x1+1 == x2) and (y1+indicator == y2)):
            print("3")
            return True
    except:
        print()

    try:
        if((board[x1-1][y1+indicator].currentPiece != ""and (x1-1 == x2) and (y1+indicator == y2))):
            print("4")
            return True 
    except:
        print()

    return False

def rookCheck(board, x1, y1, x2, y2):
    #TODO: allow for castling with the king
    if(bool(x1 == x2) != bool(y1 == y2)):
        if (x1 > x2):
            i = x2
            j = x1
            print("1")
        elif (x1 < x2):
            i = x1
            j = x2
            print("2")
        elif (y1 > y2):
            i = y2
            j = y1
            print("3")
        elif (y1 < y2):
            i = y1
            j = y2
            print("4")
        print(i,j)
        for check in range(i+1,j):   
            if ((x1 > x2) or (x1 < x2)):
                if (board[check][y1].currentPiece != ""):
                    return False
            elif ((y1 > y2) or (y1 < y2)):
                if (board[x1][check].currentPiece != ""):
                    return False
            print(check)
        return True

    return False

def knightCheck(board, x1, y1, x2, y2):
    if(abs(x1-x2)==2 and ((y2 == y1-1)or(y2 == y1+1))):
        return True
    elif(abs(y1-y2)==2 and ((x2 == x1-1)or(x2 == x1+1))):
        return True
    return False
    
def bishopCheck(board, x1, y1, x2, y2):
    if (abs(x1-x2) == abs(y1-y2)):
        xInd = int(x2-x1)/abs(x1-x2)
        yInd = int(y2-y1)/abs(y1-y2)

        distance = abs(x1-x2)
        print(xInd, yInd, distance)
        for i in range(1, distance):
            print(x1+(xInd*i))
            print(y1+(yInd*i))
            if (board[int(x1+(xInd*i))][int(y1+(yInd*i))].currentPiece != ""):
                return False
        return True
    return False

def queenCheck(board, x1, y1, x2, y2):
    return (pawnCheck(board, x1, y1, x2, y2) or rookCheck(board, x1, y1, x2, y2) or bishopCheck(board, x1, y1, x2, y2) or kingCheck(board, x1, y1, x2, y2))

def kingCheck(board, x1, y1, x2, y2):
    if (((x1 == x2) or (x1-1 == x2) or (x1+1 == x2)) and ((y1 == y2) or (y1-1 == y2) or (y1+1 == y2))):
        return True
    return False



def main():
    w, h = 8, 8
    board = [[0 for x in range(w)] for y in range(h)]

    win = GraphWin("Chess",800,800)

    
    board = buildBoard(win, board)
##white-pawns------------------------------------------------------------------
    for i in range(8):
        board[i][6].currentPiece = Piece("w", "p", Image(Point(board[i][6].xpos,board[i][6].ypos), "w_pawn.png"), board[i][6].xpos, board[i][6].ypos, "w_pawn.png")
        board[i][6].currentPiece.image.draw(win)    
##the-rest-of-white-------------------------------------------------------------
    board[0][7].currentPiece = Piece("w", "r", Image(Point(board[0][7].xpos,board[0][7].ypos), "w_rook.png"), board[0][7].xpos, board[0][7].ypos, "w_rook.png")
    board[0][7].currentPiece.image.draw(win)
    board[1][7].currentPiece = Piece("w", "n", Image(Point(board[1][7].xpos,board[1][7].ypos), "w_nigh.png"), board[1][7].xpos, board[1][7].ypos, "w_nigh.png")
    board[1][7].currentPiece.image.draw(win)
    board[2][7].currentPiece = Piece("w", "b", Image(Point(board[2][7].xpos,board[2][7].ypos), "w_bish.png"), board[2][7].xpos, board[2][7].ypos, "w_bish.png")
    board[2][7].currentPiece.image.draw(win)
    board[3][7].currentPiece = Piece("w", "q", Image(Point(board[3][7].xpos,board[3][7].ypos), "w_quee.png"), board[3][7].xpos, board[3][7].ypos, "w_quee.png")
    board[3][7].currentPiece.image.draw(win)
    board[4][7].currentPiece = Piece("w", "k", Image(Point(board[4][7].xpos,board[4][7].ypos), "w_king.png"), board[4][7].xpos, board[4][7].ypos, "w_king.png")
    board[4][7].currentPiece.image.draw(win)
    board[5][7].currentPiece = Piece("w", "b", Image(Point(board[5][7].xpos,board[5][7].ypos), "w_bish.png"), board[5][7].xpos, board[5][7].ypos, "w_bish.png")
    board[5][7].currentPiece.image.draw(win)
    board[6][7].currentPiece = Piece("w", "n", Image(Point(board[6][7].xpos,board[6][7].ypos), "w_nigh.png"), board[6][7].xpos, board[6][7].ypos, "w_nigh.png")
    board[6][7].currentPiece.image.draw(win)
    board[7][7].currentPiece = Piece("w", "r", Image(Point(board[7][7].xpos,board[7][7].ypos), "w_rook.png"), board[7][7].xpos, board[7][7].ypos, "w_rook.png")
    board[7][7].currentPiece.image.draw(win)
##black-pawns-------------------------------------------------------------------
    for i in range(8):
        board[i][1].currentPiece = Piece("b", "p", Image(Point(board[i][1].xpos,board[i][1].ypos), "b_pawn.png"), board[i][1].xpos, board[i][1].ypos, "b_pawn.png")
        board[i][1].currentPiece.image.draw(win)
##the-rest-of-black------------------------------------------------------------
    board[0][0].currentPiece = Piece("b", "r", Image(Point(board[0][0].xpos,board[0][0].ypos), "b_rook.png"), board[0][0].xpos, board[0][0].ypos, "b_rook.png")
    board[0][0].currentPiece.image.draw(win)
    board[1][0].currentPiece = Piece("b", "n", Image(Point(board[1][0].xpos,board[1][0].ypos), "b_nigh.png"), board[1][0].xpos, board[1][0].ypos, "b_nigh.png")
    board[1][0].currentPiece.image.draw(win)
    board[2][0].currentPiece = Piece("b", "b", Image(Point(board[2][0].xpos,board[2][0].ypos), "b_bish.png"), board[2][0].xpos, board[2][0].ypos, "b_bish.png")
    board[2][0].currentPiece.image.draw(win)
    board[3][0].currentPiece = Piece("b", "q", Image(Point(board[3][0].xpos,board[3][0].ypos), "b_quee.png"), board[3][0].xpos, board[3][0].ypos, "b_quee.png")
    board[3][0].currentPiece.image.draw(win)
    board[4][0].currentPiece = Piece("b", "k", Image(Point(board[4][0].xpos,board[4][0].ypos), "b_king.png"), board[4][0].xpos, board[4][0].ypos, "b_king.png")
    board[4][0].currentPiece.image.draw(win)
    board[5][0].currentPiece = Piece("b", "b", Image(Point(board[5][0].xpos,board[5][0].ypos), "b_bish.png"), board[5][0].xpos, board[5][0].ypos, "b_bish.png")
    board[5][0].currentPiece.image.draw(win)
    board[6][0].currentPiece = Piece("b", "n", Image(Point(board[6][0].xpos,board[6][0].ypos), "b_nigh.png"), board[6][0].xpos, board[6][0].ypos, "b_nigh.png")
    board[6][0].currentPiece.image.draw(win)
    board[7][0].currentPiece = Piece("b", "r", Image(Point(board[7][0].xpos,board[7][0].ypos), "b_rook.png"), board[7][0].xpos, board[7][0].ypos, "b_rook.png")
    board[7][0].currentPiece.image.draw(win)
##-----------------
    test = 0
    end = 0
    moveChecks = {
        "p" : pawnCheck,
        "r" : rookCheck,
        "n" : knightCheck,
        "b" : bishopCheck,
        "q" : queenCheck,
        "k" : kingCheck
    }
    while (end == 0):
##getting the inital click and determining which piece was clicked            
        click = win.getMouse()
        print(click.getX(), click.getY())
        for i in range(8):
            for j in range (8):
                if (board[i][j].getClicked(click)):
                    ##saves the x and y position for use later.
                    print(i, j)
                    x1 = i
                    y1 = j
                    
                    if (board[i][j].currentPiece == ""):
                        break
                    board[i][j].currentPiece.image.undraw()

                    ##highlights which piece is selected
                    indicateSelected = Rectangle(Point(board[i][j].botxpos, board[i][j].botypos), Point(board[i][j].topxpos, board[i][j].topypos))
                    indicateSelected.setFill("red")
                    indicateSelected.draw(win)
                    board[i][j].currentPiece.image.draw(win)
           
        if (board[x1][y1].currentPiece != ""):


            click2 = win.getMouse()
            indicateSelected.undraw()
            test = test + 1
            for k in range(8):
                for l in range (8):
                ##print( board[i][j].botypos, board[i][j].topypos)
                    if (board[k][l].getClicked(click2)):
                    
                        print(k, l)
                        if(x1 == k and y1 == l):
                            break

                        print(moveChecks[board[x1][y1].currentPiece.title](board, x1, y1, k, l))
                        print((board[x1][y1].currentPiece != ""))
                        if (moveChecks[board[x1][y1].currentPiece.title](board, x1, y1, k, l)):
                                
                            if (board[k][l].currentPiece != ""):
                                if (board[k][l].currentPiece.colour == board[x1][y1].currentPiece.colour):
                                    break
                                board[k][l].currentPiece.image.undraw()
                                
                                if (board[k][l].currentPiece.title == "k"):
                                    end = 1

                        

                            board[x1][y1].currentPiece.image.undraw()
                            board[k][l].currentPiece = Piece(board[x1][y1].currentPiece.colour, board[x1][y1].currentPiece.title, Image(Point(board[k][l].xpos,board[k][l].ypos), board[x1][y1].currentPiece.pieceImage), board[k][l].xpos, board[k][l].ypos, board[x1][y1].currentPiece.pieceImage)
                            board[x1][y1].currentPiece = ""
                            board[k][l].currentPiece.image.draw(win)
                            ##selected = board[k][l].currentPiece



    endGame = Text(Point(400,400), "Game Over")
    endGame.setSize(36)

    endGame.draw(win)
    win.getMouse()
    win.close()

main()