# Q.py
from collections import defaultdict

class Q:
    def __init__(self, alpha=0.5, discount=0.5):
        self.alpha = alpha
        self.discount = discount
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

    def update(self, state, action, next_state, reward):
        current_value = self.values[state][action]
        
        v = list(self.values[next_state].values())
        next_q = max(v) if v else 0

        new_value = current_value + self.alpha * (reward + self.discount * next_q - current_value)
        self.values[state][action] = new_value

    def get_best_action(self, state):
        if state not in self.values or not self.values[state]:
            return None
        # obtener acción con Q más alto
        return max(self.values[state], key=lambda a: self.values[state][a])
