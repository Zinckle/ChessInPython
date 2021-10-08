from graphics import *

class Piece:
    colour = "" ##b for black, w for white
    title = ""  ## Pawn, King, Queen, Rook, Bishop, kNight
    image = "" #assign the image for the respective piece
    xpos = "" ##position in the x axis
    ypos = "" ##position in the y axis

    def __init__(self, c, t, i):
        self.colour = c   
        self.title = t
        self.image = i

    def setX(self, x):
        self.xpos = x   

    def setX(self, y):
        self.ypos = y   

class Square:
    colour = "" ## black or white square
    xpos = "" ##position in the x axis
    ypos = "" ##position in the y axis
    currentPiece = "" ##what peice is in this position

def buildBoard(win):
    for i in range(1,9):
        if (i % 2 != 0):
            q = 1
        else:
            q = 0

        
        for j in range(8):
            rect = Rectangle(Point(0+(100*(i-1)), 0+(100*j)), Point(100+(100*(i-1)), 100+(100*j)))
            rect.draw(win)
            if ((j+q) % 2 == 0):
                rect.setFill('White')
            else:
                rect.setFill('dark grey')


def main():
    print ("hi")
    wp = Piece("w", "p", "w_pawn.png")

    w, h = 8, 8
    board = [[0 for x in range(w)] for y in range(h)]

    win = GraphWin("Chess",800,800)

    
    buildBoard(win)
    myImage = Image(Point(50,50), wp.image)
    myImage.draw(win)      
    
    win.getMouse()
    win.close()

main()