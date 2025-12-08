class TictactoeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Board:
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "X"

    def __str__(self):
        s = ""
        s += " " + self.board_array[0][0] + " | " + self.board_array[0][1] + " | " + self.board_array[0][2] + "\n"
        s += "-----------\n"
        s += " " + self.board_array[1][0] + " | " + self.board_array[1][1] + " | " + self.board_array[1][2] + "\n"
        s += "-----------\n"
        s += " " + self.board_array[2][0] + " | " + self.board_array[2][1] + " | " + self.board_array[2][2] + "\n"
        return s

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        index = Board.valid_moves.index(move_string)
        row = index // 3
        col = index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        for i in range(3):
            if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2] != " ":
                return True, self.board_array[i][0] + " wins!"

        for i in range(3):
            if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i] != " ":
                return True, self.board_array[0][i] + " wins!"

        if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2] != " ":
            return True, self.board_array[0][0] + " wins!"

        if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0] != " ":
            return True, self.board_array[0][2] + " wins!"

        full = True
        for row in self.board_array:
            for cell in row:
                if cell == " ":
                    full = False

        if full:
            return True, "Cat's Game"

        return False, self.turn + "'s turn"


board = Board()

while True:
    print(board)
    done, message = board.whats_next()
    print(message)

    if done:
        break

    move = input("Enter move: ")

    try:
        board.move(move)
    except TictactoeException as e:
        print(e)
