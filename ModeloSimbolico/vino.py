from sklearn.datasets import load_wine   # base de datos del vino con 178 muestras , 13 características y 3 clases
from sklearn.tree import DecisionTreeClassifier, export_text # clasificador de árbol de decisión
from sklearn.model_selection import train_test_split # para dividir los datos en conjuntos de entrenamiento y prueba

# Cargamos los datos del vino
vino = load_wine()
caracteristicas, clases = vino.data, vino.target

# Dividimos los datos en entrenamiento 80% y prueba en  20%
entrenamiento1, datos1, entrenamiento2, datos2 = train_test_split(
    caracteristicas, clases, test_size=0.2, random_state=42
)

# Creamos y entrenamos el clasificador de árbol de decisión
arbol = DecisionTreeClassifier(max_depth=None, random_state=42)
arbol.fit(entrenamiento1, entrenamiento2)

# Mostrar las reglas del árbol de decisión
reglas = export_text(arbol, feature_names=vino.feature_names)
print("Reglas:\n")
print(reglas)

# Evaluamos el modelo en los datos de prueba
precision = arbol.score(datos1, datos2)
print("Precisión:", precision)

