class Gato:
    def __init__(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.player = 1
        self.repr = {0: ".", 1: "x", -1: "o"}

    def get_winner(self):
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                return self.board[i][0]
        for i in range(3):
            if abs(sum(self.board[j][i] for j in range(3))) == 3:
                return self.board[0][i]
        d1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        d2 = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if abs(d1) == 3:
            return self.board[1][1]
        if abs(d2) == 3:
            return self.board[1][1]
        return None

    def get_state(self):
        return str(self.board)

    def get_valid_actions(self):
        acciones = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    acciones.append((i, j))
        return acciones

    def is_ended(self):
        if self.get_winner() is not None:
            return True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def _print(self):
        for fila in self.board:
            print(" ".join(self.repr[x] for x in fila))
        print()

    def play(self, x, y):
        if self.board[x][y] != 0:
            return None
        self.board[x][y] = self.player
        ganador = self.get_winner()
        if ganador:
            return ganador
        self.player *= -1
        return None

    def reiniciar(self):
        self.board = [[0, 0, 0] for _ in range(3)]
        self.player = 1
