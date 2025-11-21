class Gato:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.player = 1  # 1 = agente, -1 = oponente
        self.repr = {0: ".", 1: "x", -1: "o"}

    def get_winner(self):
        # filas
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                return self.board[i][0]

        # columnas
        for i in range(3):
            col_sum = sum(self.board[j][i] for j in range(3))
            if abs(col_sum) == 3:
                return self.board[0][i]

        # diagonal principal
        diag1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if abs(diag1) == 3:
            return self.board[1][1]

        # diagonal secundaria
        diag2 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if abs(diag2) == 3:
            return self.board[1][1]

        return None

    def get_state(self):
        return str(self.board)

    def get_valid_actions(self):
        actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    actions.append((i, j))
        return actions

    def is_ended(self):
        if self.get_winner() is not None:
            return True

        # si hay celdas vacías, no termina
        for row in self.board:
            if 0 in row:
                return False

        return True  # empate

    def _print(self):
        print("\n".join(" ".join(self.repr[cell] for cell in row) for row in self.board))
        print()

    def play(self, x, y):
        if self.board[x][y] != 0:
            return None

        self.board[x][y] = self.player
        winner = self.get_winner()

        if winner is not None:
            return winner

        # cambia turno
        self.player *= -1
        return None
