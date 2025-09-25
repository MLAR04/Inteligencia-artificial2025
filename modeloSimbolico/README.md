Breve explicación de el clasificador y el dataset:
Wine Data:
1. El árbol de decisión es un modelo simbólico
porque:
a. Clasifica los datos siguiendo reglas condicionales del tipo
si-entonces.
b. Cada nodo del árbol representa una pregunta sobre una
característica (ejemplo: ¿alcohol ≤ 12.8?).
c. Las ramas son las respuestas (sí o no).
d. Las hojas finales representan la clase asignada (tipo de
vino).

2. El Wine dataset (incluido en scikit-learn) es un
conjunto de datos clásico de clasificación:
● Contiene 178 muestras de vino.
● Cada vino tiene 13 características químicas medidas en
laboratorio, como:
○ Alcohol
○ Ácido málico
○ Cenizas
○ Magnesio
○ Flavonoides
○ Proline (aminoácido relacionado con la uva)
● Los vinos están clasificados en 3 clases (0, 1, 2) que representan 3
tipos de vino cultivados en la región italiana de Piamonte.
Objetivo de la práctica
● Aprender a entrenar un árbol de decisión como clasificador
simbólico.
● Comprender cómo el modelo genera reglas lógicas
interpretables.
● Explorar un dataset real (vino) y analizar sus características.
Instrucciones paso a paso
● Importar librerías necesarias:
○ from sklearn.datasets import load_wine
○ from sklearn.tree import DecisionTreeClassifier, export_text

○ from sklearn.model_selection import train_test_split

Estas librerías permiten:
● load_wine → cargar la base de datos del vino.
● DecisionTreeClassifier → crear el clasificador basado en
reglas.
● export_text → visualizar las reglas aprendidas.
● train_test_split → dividir los datos en entrenamiento y
prueba.

● Cargar el dataset del vino:
○ wine = load_wine()
○ x, y = wine.data, wine.target
Donde:

● x contiene las características químicas del vino (ej.
alcohol, ácido málico, flavonoides, etc.)
● y contiene la clase del vino (0, 1 o 2, que corresponden
a 3 tipos de vino).

● Dividir los datos en entrenamiento y prueba
○ 80% de los datos se usan para entrenar.
○ 20% se reservan para probar la precisión.
● Crear y entrenar el clasificador
● max_depth=2 limita la profundidad del árbol para que las
reglas sean más fáciles de interpretar.
● Exportar y visualizar las reglas simbólicas
○ rules = export_text(tree, feature_names=wine.feature_names)
○ print(rules)

Actividades
● Cambia el parámetro max_depth de DecisionTreeClassifier y
observa cómo cambian las reglas del árbol.
● Prueba a entrenar el modelo sin limitar la profundidad
(max_depth=None). ¿Qué notas en las reglas?
● Evalúa la precisión del modelo en los datos de prueba:
○ print("Precisión en datos de prueba:", tree.score(X_test,
y_test))

● Cuales son tus opiniones de los resultados.

Realice pruebas cambiando el porcentaje de los datos para pruebas
en 10%, 20% (el solicitado) y 40%
Los resultados me dieron:
10% = Precisión en datos de prueba: 0.8888888888888888
20% = Precisión en prueba: 0.9444444444444444
40% = Precisión en datos de prueba: 0.9305555555555556
Esto muestra que en realidad si es mas optimo hacer una división de
80-20 para entrenamiento-prueba:
Al tener menos datos de prueba no podemos comprobar la fiabilidad
del modelo (Por eso el de 10% de datos de prueba solo arroja el 88% de
éxito).
Cuando le damos más datos de prueba (40% por ejemplo), será precisa
pero no considerablemente fiable, ya que casi la mitad de los datos
probados son parte de los datos totales, sacrificamos datos de
entrenamiento sobre prueba, a la larga esto no seria fiable.
