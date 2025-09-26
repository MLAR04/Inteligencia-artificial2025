# PRÁCTICA DE RECURSIVIDAD

## Descripción
Este programa es un script que contiene dos funciones recursivas. Una para generar la sucesión de Fibonacci hasta n números y otra para calcular el factorial de un número. La finalidad de la práctica es comprender su importancia en la inteligencia artificial, ya que muchos algoritmos se basan en dividir problemas en subproblemas mas simples.

## Requisitos para correr el script:
  - Python 3.12.3 o superior.

## Instrucciones para ejecutar el script
1. Clonar el repositorio.
2. Desde la linea de comandos, abrir el directorio donde se encuentra este proyecto.
3. Ejecutar **python3 practicaRecursiva.py**

## Uso de las funciones

### fibonacci(n)
Genera la secuencia de Fibonacci hasta n elementos de forma recursiva. Devuelve una lista 
con los primeros n números de la secuencia. La función retorna un arreglo, asi que la llamada a la función hay que asignarla en un print para ver el resultado.

- Parámetros:
  - "n" (int): Cantidad de números a generar en la secuencia
- Ejemplo:
print(fibonacci(5))
**Salida:** [1, 1, 2, 3, 5]


### factorial(n)
Realiza el calculo del factorial de un número de forma recursiva. Devuelve el valor del
factorial y la secuencia de multiplicaciones que se hicieron para llegar al resultado.

- Parámetros:
  - "n" (int): Número entero del cual se desea calcular el factorial.
- Ejemplo:
secuencia,valor=factorial(7)
print(f"Factorial: {valor}, Secuencia: {secuencia}")
**Salida:** Factorial: 5040, Secuencia: [1, 2, 3, 4, 5, 6, 7]