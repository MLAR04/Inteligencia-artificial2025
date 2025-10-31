# Práctica de Q-Learning

## Objetivo : Crear agente para el juego del gato mediante entrenamiento con refuerzo.

Reglas del Juego:

- Como tablero se utiliza una matriz de 3 X 3
- El Juego es por Turnos
- Son 2 Jugadores por Partida
- Cada jugador escoge una posición dentro de las dimensiones de la matriz, si el espacio seleccionado no está disponible entonces debe seleccionar otro.

## El juego termina cuando:

- Uno de los jugadores completa 3 espacios consecutivos de manera horizontal o de manera vertical.
- Ya no existen más posiciones disponibles dentro del tablero.

## Instrucciones:

Genera un archivo para la clase del juego que contenga:

- **init**
- get_winner
- get_state
- get_valid_actions
- is_ended
- \_print
- play

### Explicación:

- Usaremos 1 para el primer jugador y -1 para el segundo jugador. la play función acepta x y y como argumentos y coloca el movimiento del jugador actual en esas coordenadas en el tablero de 3x3 del juego y luego cambia el turno al otro jugador.
- Si tenemos un ganador, devolverá el ganador; de lo contrario, volverá None.
- La lógica para detectar al ganador está en la get_winner función. (Simplemente verifica las ganancias primero en filas, luego en columnas)
- La función is_ended comprueba si queda alguna celda vacía en el tablero y regresa si el juego ha terminado o no.
- La función get_valid_actions devuelve todas las coordenadas de celdas vacías.
- La estructura del juego es la siguiente: debemos llamar a la función play en un bucle hasta que tengamos un ganador o el juego termine en empate.

## Código:

class Gato:

def **init**(self):
self.board = [[0, 0, 0] for \_ in range(3)]
self.player = 1
self.repr = {0: ".", 1: "x", -1: "o"}

def get_winner(self): # check horizontal
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

### Genera un archivo para el aprendizaje:

En cada turno, nuestro agente de IA debe tomar una decisión sobre qué celda elegir para realizar su movimiento. Para hacerlo, debe tener una estimación de las recompensas para cada par “(state, action)” para que pueda elegir la acción que resulte en la recompensa máxima. La tabla Q contendrá estas estimaciones de manera que:
Q[state][action] -> reward estimation.

### Proceso de aprendizaje :

El agente obtiene el estado actual del juego y elige una acción. Al principio, los valores de Q no se actualizan y queremos que el agente explore el juego. El agente aplica la acción elegida al juego. Luego, como oponente, jugamos un movimiento aleatorio. Ahora tenemos un nuevo estado. Si el agente gana, tenemos una recompensa de 100. Si pierde, usamos -100 como recompensa. de lo contrario, la recompensa es 0.

### Ahora podemos actualizar el valor Q(state, action) con esta fórmula:

Q(S,A) = Q(S,A) + α ∗ (R + γ ∗ maxQ(S′,a) − Q(S,A)).

### Donde:

- S es el estado actual
- R es la recompensa instantánea que obtuvimos después de aplicar la acción.
- A es la acción elegida,
- α es el tamaño del peso. lo que significa cuánto peso queremos dar al nuevo valor en comparación con el valor actual.
  γ es el factor de descuento.
- maxQ(S′,a)es el valor máximo de Q sobre todas las acciones para el nuevo estado.
- Repita los 3 pasos anteriores hasta que las estimaciones de Q sean lo suficientemente buenas.
  Codigo

### class Q:

- def **init**(self, alpha=0.5, discount=0.5):
- self.alpha = alpha
- self.discount = discount
- self.values = defaultdict(lambda: defaultdict(lambda: 0.0))
