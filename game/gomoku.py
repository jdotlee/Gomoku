
class Game:
    SIZE = 15
    def __init__(self):
        self.board = [[0] * 15 for _ in range(15)]
        self.turn = 1
        self.gameOver = False
        self.won = 0
    
    def place(self, x, y):
        if self.board[y][x] == 0 and x < 15 and y < 15 and x >= 0 and y >= 0:
            self.board[y][x] = self.turn
            self.winner(self.turn)
            return True
        else:
            print("Invalid Move Choice, Try Again!")
            return False

    def nextTurn(self):
        self.turn = self.turn % 2 + 1

    def winner(self, player):
        # horizontal check
        for x in range(len(self.board) - 4) :
            for y in range(len(self.board)):
                if (self.board[y][x] == player and self.board[y][x + 1] == player and self.board[y][x + 2] == player
                and self.board[y][x + 3] == player and self.board[y][x + 4] == player) :
                
                    self.gameOver = True
                    return True


        # vertical check
        for y in range(len(self.board) - 4) :
            for x in range(len(self.board)):
                if (self.board[y][x] == player and self.board[y + 1][x] == player and self.board[y + 2][x] == player
                and self.board[y + 3][x] == player and self.board[y + 4][x] == player) :
                
                    self.gameOver = True
                    self.won = player
                    return True

        # ascending diagonal check
        for y in range(4, len(self.board)) :
            for x in range(len(self.board) - 4):
                if (self.board[y][x] == player and self.board[y - 1][x + 1] == player and self.board[y - 2][x + 2] == player
                and self.board[y - 3][x + 3] == player and self.board[y - 4][x + 4] == player) :
                
                    self.gameOver = True
                    self.won = player
                    return True


        # descending diagonal check
        for y in range(4, len(self.board)) :
            for x in range(4, len(self.board)):
                if (self.board[y][x] == player and self.board[y - 1][x - 1] == player and self.board[y - 2][x - 2] == player
                and self.board[y - 3][x - 3] == player and self.board[y - 4][x - 4] == player) :

                    self.gameOver = True
                    self.won = player
                    return True
        return False

    def __str__(self):
        toReturn = ""
        for row in range(len(self.board)):
            if row < 10:
                toReturn += "\n   -------------------------------------------------------------\n" + str(row) + "  |"
            else:
                toReturn += "\n   -------------------------------------------------------------\n" + str(row) + " |"
            for item in self.board[row]:
                if item == 0:
                    toReturn += "   |"
                elif item == 1:
                    toReturn += "⚫ |"#" • |"
                elif item == 2:
                    toReturn += " ⚪|"#" ○ |"
            
        return "     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  \n" + toReturn + "\n   -------------------------------------------------------------\n"

def play():
    game = Game()
    print(game)
    while not game.gameOver:
        if game.turn == 1:
            print("Black's Turn")
        else:
            print("White's Turn")

        valid = False
        while not valid:
            x = int(input("Input X Coor:"))
            y = int(input("Input Y Coor:"))
            valid = game.place(x, y)
        print(game)
        game.nextTurn()
    if game.won == 1:
        print("Black Wins!!!")
    else:
        print("White Wins!!!")

