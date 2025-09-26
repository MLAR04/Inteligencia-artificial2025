# PRÁCTICA DE MODELO SIMBÓLICO

## Descripción
Este programa implementa un árbol de decisión haciendo uso del dataset de vinos 'wine' 
incluido en la librería scikit-learn. El árbol de decisión aprende reglas que permiten
clasificar cada vino en su categoría dependiendo de sus características (13 en total).
El script muestra las reglas generadas por el árbol así como la precisión del modelo
sobre el porcentaje que se usa para los datos de prueba.

## Requisitos para correr el script:
  - Python 3.12.3 o superior.
  - librería scikit-learn
  - Un entorno virtual de python (opcional). Esto es recomendable para aislar el proyecto y poder instalar distintas versiones de librerías sin afectar la instalación global de Python.

## Instrucciones para ejecutar el script
1. Clonar el repositorio.
2. Desde la línea de comandos, abrir el directorio donde se encuentra este proyecto.
3. Crear un venv para nuestro proyecto (Entorno virtual de Python) con el comando **python3 -m venv venv**
4. Entrar al entorno virtual con el comando **source venv/bin/activate**
5. En el venv, instalar la librería scikit-learn con **pip install scikit-learn**
6. Ejecutar el script dentro de nuestro venv: **python3 modelo-simbolico.py**
7. Si desea salir del entorno virtual, simplemente escriba **deactivate** en la línea de comandos

## Uso de los parámetros para entrenar el árbol
Por defecto, este script usa el 80% de la información para entrenar el modelo y 20% para pruebas. Sin embargo, el usuario puede modificar dichos parámetros si lo desea, así como también modificar la profundidad máxima del árbol.


### **max_depth** en DecisionTreeClassifier 
 - Define la profundidad máxima que puede tener el árbol. A mayor profundidad, el árbol se vuelve más complejo. Un valor pequeño hace un árbol más simple y general.

### **random_state** en train_test_split
 - Controla la semilla aleatoria para dividir los datos en entrenamiento y prueba. Útil si
 varios usuarios corren este mismo script y quieren obtener las mismas divisiones de datos.

### **test_size** en train_test_split
 - Define el porcentaje de datos que se reserva para las pruebas. El resto del porcentaje
 se usa para entrenar el modelo.
