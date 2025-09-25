from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Cargar datos
wine = load_wine()
X, y = wine.data, wine.target

# Entrenamiento y prueba donde test_size=0.x es el porcentaje de datos para prueba, random_state=42 sirve para reproducibilidad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=42)

# Entrenar el modelo de árbol de decisión con profundidad máxima de 3
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

# Visualización del árbol de decisión
print(export_text(tree, feature_names=wine.feature_names))

# Evaluar el modelo en datos de prueba y mostrar precisión
print("Precisión en datos de prueba:", tree.score(X_test, y_test))