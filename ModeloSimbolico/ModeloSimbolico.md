# Introducción
En esta practica utilizaremos la librería SciKitLearn en conjunto con la base de datos Wine para generar un modelo simbolico el cual utilice arboles de desicion, se modificarán distintos parámetros antes de entrenar el modelo y se anotarán los resultados observados.

### Paso 1: 
Se importan las librerías de SciKit que se van a utilizar, en este caso, la base de datos de vino, la función de árbol de decisiones, función de exportación de texto y la función para separar datos de entrenamiento y de prueba.

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

### Paso 2: 
Cargamos la base de datos

wine = load_wine()
data, target = wine.data,wine.target

### Paso 3: 
Separamos los datos con la función train_test_split

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

### Paso 4: 
Entrenamos nuestro modelo con la función DecisionTreeClassifier() y le pasamos los datos que separamos para entrenamiento.

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

### Paso 5: 
Mostramos el arbol de reglas que fueron generadas utilizando la función export_text

rules = export_text(model, feature_names=wine.feature_names)
print(rules)

### Paso 6: 
Mostramos que tan preciso es el modelo generado utilizando la función model(score) y pasando como argumento nuestros datos de prueba

print("Accuracy: ", model.score(X_test, y_test))



### Resultados:

|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- ash <= 3.07
|   |   |   |--- class: 1
|   |   |--- ash >  3.07
|   |   |   |--- class: 0
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- proline <= 724.50
|   |   |   |--- malic_acid <= 3.92
|   |   |   |   |--- class: 1
|   |   |   |--- malic_acid >  3.92
|   |   |   |   |--- class: 0
|   |   |--- proline >  724.50
|   |   |   |--- class: 0

Accuracy:  0.9444444444444444


### Conclusión:

Al entrenar el modelo y ejecutar el programa, nos muestra el árbol de reglas que está siguiendo para determinar la clase de vino. Sin restricciones de tamaño del árbol se logra una certeza de 94%.




## Actividades

## Actividad 1. 
Cambia el parámetro max_depth de DecisionTreeClassifier y observa cómo cambian las reglas del árbol.

### Paso 1: 
Cambiaremos la profundidad a 1.

model = DecisionTreeClassifier(max_depth=1)
model.fit(X_train, y_train)

### Resultado:

|--- color_intensity <= 3.82
|   |--- class: 1
|--- color_intensity >  3.82
|   |--- class: 0

Accuracy:  0.6666666666666666


### Paso 2: 
Cambiaremos la profundidad a 2.

### Resultado:

|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- class: 1
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- class: 0

Accuracy:  0.8611111111111112

## Conclusión:

Limitar la profundidad de los arboles hace más rápido el procesamiento, pero esto nos deja con una precisión más baja, de un 66% con una profundidad de 1 y 86% con una profundidad de 2. Es interesante notar la jerarquía de características que se toman en cuenta, por ejemplo, la intensidad de color es considerado el factor más importante.



## Actividad 2. 
Prueba a entrenar el modelo sin limitar la profundidad (max_depth=None). ¿Qué notas en las reglas?

model = DecisionTreeClassifier(max_depth=None)
model.fit(X_train, y_train)

### Resultado:

|--- color_intensity <= 3.82
|   |--- proline <= 1002.50
|   |   |--- ash <= 3.07
|   |   |   |--- class: 1
|   |   |--- ash >  3.07
|   |   |   |--- class: 0
|   |--- proline >  1002.50
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.40
|   |   |--- class: 2
|   |--- flavanoids >  1.40
|   |   |--- proline <= 724.50
|   |   |   |--- malic_acid <= 3.92
|   |   |   |   |--- class: 1
|   |   |   |--- malic_acid >  3.92
|   |   |   |   |--- class: 0
|   |   |--- proline >  724.50
|   |   |   |--- class: 0

Accuracy:  0.9444444444444444

## Conclusión:
Nos da la misma respuesta que no entrenarlo con un parámetro específico de profundidad, por lo que se puede concluir que con este set especifico de datos y este método específico, la mejor certeza con la que se puede predecir la calidad de un vino es de 94%
