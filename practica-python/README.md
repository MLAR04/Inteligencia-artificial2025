# PRÁCTICA DE PYTHON

## Descripción
Este programa es un ejemplo básico de programación lógica enfocado a los
conceptos de hechos, reglas y consultas. Consiste en mostrar relaciones
familiares sencillas entre personas con hechos definidos.

## Requisitos para correr el script:
  - Python 3.12.3 o superior.

## Instrucciones para ejecutar el script
1. Clonar el repositorio.
2. Desde la linea de comandos, abrir el directorio donde se encuentra este proyecto.
3. Ejecutar |python3 practicaPython.py|

## Uso de las funciones
Para usar cada una de las funciones del script, el usuario debe basarse en los hechos
definidos en el diccionario "padres". Cuando el usuario mande a llamar cada una de las funciones, al pasarle los argumentos, debe de hacerlo en base a los hechos definidos en el diccionario. Por ejemplo, para referirse a un hijo, debe escribir el nombre exactamente como está definido en el diccionario.

### son_hermanos(x,y) 
Verifica si "x" y "y" son hermanos.

- Parámetros:
  - "x" (str): nombre del primer hijo
  - "y" (str): nombre del segundo hijo
- Ejemplo:
son_hermanos("Patricia","Esther");
#Salida: Patricia y Esther son Hermanos

### es_hijo_de(x,padre) 
Verifica si "x" es hijo de "padre".

- Parámetros:
  - "x" (str): nombre del hijo
  - "padre" (str): nombre del padre
- Ejemplo:
es_hijo_de("Patricia","Raul");
**Salida** 
Patricia es hij@ de Raul


### sus_hijos_son(padre)
Verifica que el padre exista, y de ser así, imprime sus hijos.

- Parámetros:
  - "padre"  (str): nombre del padre
- Ejemplo:
es_hijo_de("Patricia","Raul");
**Salida**
Los hijos de Juan son: 
Maria
Carlos
