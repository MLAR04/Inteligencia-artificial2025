import tkinter as tk
from tkinter import messagebox
import random
import os
from gato import Gato
from agent import Agent

class InterfazGato:
    def __init__(self, root, agente):
        self.root = root
        self.agente = agente
        self.humano = 1
        self.maquina = -1
        self.juego = Gato()
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.ultimo_estado = None
        self.ultima_accion = None
        self.construir()

    def construir(self):
        marco = tk.Frame(self.root)
        marco.pack(padx=20, pady=20)
        for i in range(3):
            for j in range(3):
                b = tk.Button(marco, text="", font=("Arial", 32), width=3, height=1,
                              command=lambda x=i, y=j: self.jugada_humana(x, y))
                b.grid(row=i, column=j, padx=5, pady=5)
                self.botones[i][j] = b
        self.info = tk.Label(self.root, text="Tú eres X, el agente es O")
        self.info.pack()
        self.boton = tk.Button(self.root, text="Nueva Partida", command=self.reiniciar)
        self.boton.pack(pady=10)
        self.actualizar()

    def reiniciar(self):
        self.juego.reiniciar()
        self.ultimo_estado = None
        self.ultima_accion = None
        self.actualizar()

    def jugada_humana(self, x, y):
        if self.juego.player != self.humano:
            return
        if self.juego.board[x][y] != 0:
            return
        ganador = self.juego.play(x, y)
        self.actualizar()
        if self.ultimo_estado is not None and self.ultima_accion is not None:
            nuevo_estado = self.juego.get_state()
            if ganador == self.humano:
                recompensa = -100
            elif self.juego.is_ended():
                recompensa = 0
            else:
                recompensa = 0
            self.agente.qlearner.update(self.ultimo_estado, self.ultima_accion, nuevo_estado, recompensa)
            self.agente.guardar("qtable.pkl")
            self.ultimo_estado = None
            self.ultima_accion = None
        if ganador is not None:
            if ganador == self.humano:
                messagebox.showinfo("Gato", "Ganaste")
            else:
                messagebox.showinfo("Gato", "El agente ganó")
            return
        if self.juego.is_ended():
            messagebox.showinfo("Gato", "Empate")
            return
        self.jugada_maquina()

    def jugada_maquina(self):
        if self.juego.is_ended():
            return
        estado = self.juego.get_state()
        acciones = self.juego.get_valid_actions()
        if not acciones:
            return
        if random.random() < 0.05:
            accion = random.choice(acciones)
        else:
            mejor = self.agente.qlearner.get_best_action(estado, acciones)
            if mejor is None:
                accion = random.choice(acciones)
            else:
                accion = mejor
        ganador = self.juego.play(*accion)
        self.actualizar()
        if ganador == self.maquina:
            nuevo_estado = self.juego.get_state()
            self.agente.qlearner.update(estado, accion, nuevo_estado, 100)
            self.agente.guardar("qtable.pkl")
            messagebox.showinfo("Gato", "El agente ganó")
            return
        if self.juego.is_ended():
            nuevo_estado = self.juego.get_state()
            self.agente.qlearner.update(estado, accion, nuevo_estado, 0)
            self.agente.guardar("qtable.pkl")
            messagebox.showinfo("Gato", "Empate")
            return
        self.ultimo_estado = estado
        self.ultima_accion = accion

    def actualizar(self):
        for i in range(3):
            for j in range(3):
                v = self.juego.board[i][j]
                if v == 1:
                    t = "X"
                elif v == -1:
                    t = "O"
                else:
                    t = ""
                self.botones[i][j].config(text=t)

if __name__ == "__main__":
    agente = Agent()
    if os.path.exists("qtable.pkl"):
        try:
            agente.cargar("qtable.pkl")
        except Exception:
            agente.learn(5000)
            agente.guardar("qtable.pkl")
    else:
        agente.learn(5000)
        agente.guardar("qtable.pkl")
    raiz = tk.Tk()
    raiz.title("Gato con Q-Learning")
    app = InterfazGato(raiz, agente)
    raiz.mainloop()
