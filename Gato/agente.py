# agente.py
import random
from Q import Q
from gato import Gato

class Agent:
    def __init__(self):
        self.eps = 1.0
        self.qlearner = Q()

    def get_action(self, state, valid_actions):
        # exploración
        if random.random() < self.eps:
            return random.choice(valid_actions)

        best = self.qlearner.get_best_action(state)
        if best is None:
            return random.choice(valid_actions)
        return best

    def learn(self, episodes=10000):
        for _ in range(episodes):
            self.learn_game()
            # reducir epsilon
            if self.eps > 0.05:
                self.eps *= 0.999

    def learn_game(self):
        game = Gato()
        state = game.get_state()

        while not game.is_ended():
            valid_actions = game.get_valid_actions()

            # acción del agente
            action = self.get_action(state, valid_actions)
            winner = game.play(*action)
            next_state = game.get_state()

            # recompensa inicial
            reward = 0

            if winner == 1:
                reward = 100
            elif winner == -1:
                reward = -100

            # actualizar Q
            self.qlearner.update(state, action, next_state, reward)

            if winner is not None:
                break
            if game.is_ended():
                break

            # turno del oponente (jugada aleatoria)
            opp_actions = game.get_valid_actions()
            if opp_actions:
                opp_action = random.choice(opp_actions)
                winner = game.play(*opp_action)
                next_state2 = game.get_state()

                if winner == -1:
                    reward = -100
                elif winner == 1:
                    reward = 100
                else:
                    reward = 0

                # actualizar Q del estado anterior
                self.qlearner.update(state, action, next_state2, reward)

                if winner is not None:
                    break

            state = game.get_state()
