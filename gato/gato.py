
class Gato:
   def __init__(self):
       self.board = [[0, 0, 0] for _ in range(3)]
       self.player = 1
       self.repr = {0: ".", 1: "x", -1: "o"}




   def get_winner(self):
       # check horizontal
       for i in range(3):
           if abs(sum(self.board[i])) == 3:
               return self.board[i][0]


       # check vertical
       for i in range(3):
           if abs(sum(self.board[j][i] for j in range(3))) == 3:
               return self.board[0][i]


       return None



   def get_state(self):
       return str(self.board)






def get_valid_actions():
    



   def play(self, x, y):
       if self.board[x][y] != 0:
           return None
       self.board[x][y] = self.player


       self._print()
       winner = self.get_winner()
       if winner:
           return winner
       self.player *= -1
       return None


class Q:
   def __init__(self, alpha=0.5, discount=0.5):
       self.alpha = alpha
       self.discount = discount
       self.values = defaultdict(lambda: defaultdict(lambda: 0.0))




