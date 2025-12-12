from collections import defaultdict

class Q:
    def __init__(self, alpha=0.5, discount=0.5):
        self.alpha = alpha
        self.discount = discount
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

    def update(self, state, action, next_state, reward):
        valor = self.values[state][action]
        lista = list(self.values[next_state].values())
        siguiente = max(lista) if lista else 0
        nuevo = valor + self.alpha * (reward + self.discount * siguiente - valor)
        self.values[state][action] = nuevo

    def get_best_action(self, state, valid_actions):
        acciones = self.values[state]
        mejor = None
        val = None
        for a in valid_actions:
            q = acciones[a]
            if mejor is None or q > val:
                mejor = a
                val = q
        return mejor
