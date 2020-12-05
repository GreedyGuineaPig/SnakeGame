class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [[0 for _ in range(row)] for _ in range(col)]

    def __str__(self):
        printStr = ""
        for c in range(self.col):
            for r in range(self.row):
                printStr += str(self.board[c][r])
            printStr += "\n"
        return printStr

