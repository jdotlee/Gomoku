class Game:
    SIZE = 15
    def __init__(self):
        self.board = [[0] * 15 for _ in range(15)]
        self.turn = 1
        self.gameOver = False
        self.won = 0
    
    def place(self, x, y):
        if self.board[y][x] == 0:
            self.board[y][x] = self.turn
            return True
        else:
            print("Invalid Move Choice, Try Again!")
            return False

    def nextTurn(self):
        self.turn = self.turn % 2 + 1

    def winner(self):
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

