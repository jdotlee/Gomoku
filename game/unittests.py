import gomoku

def test_black_win():
    print("running test_black_win...")
    game = gomoku.Game()
    for i in range(5):
        game.place(0,i)

    
    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 1)
    print("     The winner should be black (1): ", game.won)



def test_white_win():
    print("running test_white_win...")
    game = gomoku.Game()
    game.nextTurn()
    for i in range(5):
        game.place(0, i)


    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 2)
    print("     The winner should be white (2): ", game.won)

def test_black_diagonal_win():
    print("running test_black_diagonal_win...")
    game = gomoku.Game()
    for i in range(5):
        game.place(i + 6, i)

    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 1)
    print("     The winner should be black (1): ", game.won)


def test_white_diagonal_win():
    print("running test_white_diagonal_win...")
    game = gomoku.Game()
    game.nextTurn()
    for i in range(5):
        game.place(i + 6, i)

    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 2)
    print("     The winner should be white (2): ", game.won)

def test_black_diagonal_win_hard():
    print("test_black_diagonal_win_hard...")
    game = gomoku.Game()
    game.place(7,7)
    game.place(8,6)
    game.place(9,5)
    game.place(10,4)
    game.place(11,3)

    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 1)
    print("     The winner should be black (1): ", game.won)


def test_white_diagonal_win_hard():
    print("test_white_diagonal_win_hard...")
    game = gomoku.Game()
    game.nextTurn()
    game.place(7, 7)
    game.place(8, 6)
    game.place(9, 5)
    game.place(10, 4)
    game.place(11, 3)

    assert(game.gameOver)
    print("     The game should be over: ", game.gameOver)
    assert(game.won == 2)
    print("     The winner should be white (2): ", game.won)

test_black_win()
test_white_win()
test_black_diagonal_win()
test_white_diagonal_win()
test_black_diagonal_win_hard()
test_white_diagonal_win_hard()
