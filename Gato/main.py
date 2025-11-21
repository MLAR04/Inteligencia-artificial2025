from agente import Agent
from gato import Gato
import random

def jugar_contra_agente(agent):
    game = Gato()

    while not game.is_ended():
        if game.player == 1:
            # turno del agente
            state = game.get_state()
            action = agent.get_action(state, game.get_valid_actions())
            game.play(*action)
            print("Agente juega:", action)
            game._print()
        else:
            # turno jugador
          
            x = int(input("x: "))
            y = int(input("y: "))
            game.play(x, y)

        if game.get_winner() is not None:
            break

    winner = game.get_winner()
    if winner == 1:
        print("El agente ganó.")
    elif winner == -1:
        print("Tú ganaste.")
    else:
        print("Empate.")

if __name__ == "__main__":
    agent = Agent()
    print("Entrenando agente...")
    agent.learn(50000)
    print("Entrenamiento completado.\n")
    jugar_contra_agente(agent)
