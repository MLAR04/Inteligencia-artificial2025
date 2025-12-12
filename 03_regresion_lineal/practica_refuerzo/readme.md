# Gato con Q-Learning  
Juego del Tic-Tac-Toe entrenado mediante **Aprendizaje por Refuerzo** (Q-Learning).  
El sistema incluye una interfaz gráfica para jugar contra un agente que **aprende**, **guarda su conocimiento**, **lo carga automáticamente**, y **mejora mientras juega**.

---

## Objetivos del proyecto
- Implementar un entorno de juego para el Gato (3x3).
- Entrenar un agente usando Q-Learning.
- Permitir que el agente siga aprendiendo durante las partidas contra el usuario.
- Guardar la tabla Q en un archivo para conservar el entrenamiento entre sesiones.
- Proveer una interfaz gráfica sencilla para interactuar con el agente.


## Archivos del proyecto

| Archivo | Función |
|--------|---------|
| `gato.py` | Lógica del juego: tablero, turnos, validación de ganador, movimientos. |
| `qlearning.py` | Implementación de la Q-table y actualización de valores Q. |
| `agent.py` | Controlador del agente: exploración, aprendizaje, guardado/carga. |
| `gui_gato.py` | Interfaz gráfica para jugar contra el agente entrenado. |
| `qtable.pkl` | Archivo generado automáticamente que guarda el aprendizaje del agente. |


## Funcionamiento del Juego (`gato.py`)

El tablero es una matriz 3×3 con estos valores:

- **1** → Jugador humano (X)  
- **–1** → Agente (O)  
- **0** → Casilla vacía  

Funciones principales:

- `get_winner()`  
  Determina si hay un ganador revisando:
  - Filas  
  - Columnas  
  - Diagonales  

- `get_state()`  
  Retorna una representación serializable del tablero, usada como clave en la Q-table.

- `get_valid_actions()`  
  Devuelve todas las coordenadas posibles donde se puede jugar.

- `is_ended()`  
  Indica si hay ganador o si el tablero está lleno.

- `play(x, y)`  
  Coloca una pieza y cambia de turno.

## Aprendizaje por Refuerzo (`agent.py`)

El agente utiliza **Q-Learning** con estrategias de exploración–explotación.

### Fórmula de actualización:

Q(S,A) = Q(S,A) + α * ( R + γ * maxQ(S′,·) − Q(S,A) )

### Recompensas:

- **+100** si el agente gana  
- **–100** si el humano gana  
- **0** en empate o jugadas internas  

### Exploración:

- El agente inicia con `eps = 1.0` (aleatorio total).
- Se reduce gradualmente con `decay = 0.995` hasta `0.05`.
- En la interfaz gráfica, mantiene un 5% de exploración para no ser predecible.


## Guardado y carga del entrenamiento

La tabla Q se guarda automáticamente en:

qtable.pkl

El agente:

- **carga** el archivo al iniciar  
- **guarda** nuevamente después de cada actualización  

Así, el aprendizaje **persiste** entre sesiones y el agente mejora a largo plazo.


## Interfaz gráfica (`main.py`)

Permite:

- Seleccionar casillas con el mouse  
- Ver movimientos del agente en tablero  
- Reiniciar partidas  
- Mantener aprendizaje continuo contra el usuario  

Durante la partida:

- El agente sigue aprendiendo con tus movimientos reales
- El archivo `qtable.pkl` se actualiza constantemente

agente.learn(5000)
Se puedde aumentar ese valor si se quiere un agente mas fuerte.

