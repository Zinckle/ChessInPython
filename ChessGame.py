
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

class Square:
    colour = "" ## black or white square
    topxpos = "" ##position in the x axis
    topypos = "" ##position in the y axis
    botxpos = "" ##position in the x axis
    botypos = "" ##position in the y axis

    xpos = "" ##position in the x axis
    ypos = "" ##position in the y axis

    currentPiece = "" ##what peice is in this position

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

##def


    #elif ((pawn.colour == "b") and  (pawn.ypos == 150)):



def main():
    print ("hi")

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
    while (end == 0):
            
        click = win.getMouse()
        print(click.getX(), click.getY())
        for i in range(8):
            for j in range (8):
            ##print( board[i][j].botypos, board[i][j].topypos)
                if (((click.getX() < board[i][j].botxpos) and (click.getX() >= board[i][j].topxpos)) and ((click.getY() < board[i][j].botypos) and (click.getY() >= board[i][j].topypos))):
                    
                    print(i, j)
                    x1 = i
                    y1 = j
                    
                    if (board[i][j].currentPiece != ""):
                        board[i][j].currentPiece.image.undraw()


                        indicateSelected = Rectangle(Point(board[i][j].botxpos, board[i][j].botypos), Point(board[i][j].topxpos, board[i][j].topypos))
                        indicateSelected.setFill("red")
                        indicateSelected.draw(win)
                        board[i][j].currentPiece.image.draw(win)

                    else: 
                        break
        print(x1,y1)           
        if (board[x1][y1].currentPiece != ""):
            click2 = win.getMouse()
            indicateSelected.undraw()
            test = test + 1
            for k in range(8):
                for l in range (8):
                ##print( board[i][j].botypos, board[i][j].topypos)
                    if (((click2.getX() < board[k][l].botxpos) and (click2.getX() >= board[k][l].topxpos)) and ((click2.getY() < board[k][l].botypos) and (click2.getY() >= board[k][l].topypos))):
                    
                        print(k, l)
                        if(x1 == k and y1 == l):
                            break

                        board[x1][y1].currentPiece.image.undraw()
                        if (board[k][l].currentPiece != ""):
                            board[k][l].currentPiece.image.undraw()
                            if (board[k][l].currentPiece.title == "k"):
                                end = 1

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