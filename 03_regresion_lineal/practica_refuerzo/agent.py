import random
import pickle
from qlearning import Q
from gato import Gato

class Agent:
    def __init__(self):
        self.eps = 1.0
        self.min_eps = 0.05
        self.decay = 0.995
        self.qlearner = Q()

    def get_action(self, state, valid_actions):
        if random.random() < self.eps:
            return random.choice(valid_actions)
        mejor = self.qlearner.get_best_action(state, valid_actions)
        if mejor is None:
            return random.choice(valid_actions)
        return mejor

    def learn_game(self):
        juego = Gato()
        while not juego.is_ended():
            estado = juego.get_state()
            acciones = juego.get_valid_actions()
            if not acciones:
                break
            accion = self.get_action(estado, acciones)
            ganador = juego.play(*accion)
            nuevo_estado = juego.get_state()
            if ganador == 1:
                recompensa = 100
                self.qlearner.update(estado, accion, nuevo_estado, recompensa)
                break
            if juego.is_ended():
                recompensa = 0
                self.qlearner.update(estado, accion, nuevo_estado, recompensa)
                break
            acciones_op = juego.get_valid_actions()
            if not acciones_op:
                recompensa = 0
                self.qlearner.update(estado, accion, nuevo_estado, recompensa)
                break
            accion_op = random.choice(acciones_op)
            ganador_op = juego.play(*accion_op)
            siguiente_estado = juego.get_state()
            if ganador_op == -1:
                recompensa = -100
                self.qlearner.update(estado, accion, siguiente_estado, recompensa)
                break
            if juego.is_ended():
                recompensa = 0
                self.qlearner.update(estado, accion, siguiente_estado, recompensa)
                break
            recompensa = 0
            self.qlearner.update(estado, accion, siguiente_estado, recompensa)

    def learn(self, partidas=5000):
        for _ in range(partidas):
            self.learn_game()
            self.eps = max(self.min_eps, self.eps * self.decay)

    def guardar(self, archivo="qtable.pkl"):
        datos = {}
        for estado, acciones in self.qlearner.values.items():
            datos[estado] = dict(acciones)
        with open(archivo, "wb") as f:
            pickle.dump(datos, f)

    def cargar(self, archivo="qtable.pkl"):
        from collections import defaultdict
        with open(archivo, "rb") as f:
            datos = pickle.load(f)
        valores = defaultdict(lambda: defaultdict(lambda: 0.0))
        for estado, acciones in datos.items():
            for accion, q in acciones.items():
                valores[estado][accion] = q
        self.qlearner.values = valores
