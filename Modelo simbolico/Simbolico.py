# Importacion de librerias

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Cargando el dataset del vino:

wine = load_wine()
x,y = wine.data, wine.target

# Dividir los datos en entrenamiento y prueba

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 4. Crear y entrenar el clasificador con profundidad máxima = 2

tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)

# 5. Exportar y visualizar las reglas aprendidas

rules = export_text(tree, feature_names=wine.feature_names)
print("=== Reglas con max_depth=2 ===")
print(rules)

# 6. Evaluar la precisión en los datos de prueba
print("Precisión en datos de prueba:", tree.score(X_test, y_test))





# # Árbol más profundo (max_depth=5)
# tree2 = DecisionTreeClassifier(max_depth=5, random_state=42)
# tree2.fit(X_train, y_train)
# rules2 = export_text(tree2, feature_names=wine.feature_names)
# print("\n=== Reglas con max_depth=5 ===")
# print(rules2)
# print("Precisión (max_depth=5):", tree2.score(X_test, y_test))

# # Árbol sin límite de profundidad
# tree3 = DecisionTreeClassifier(max_depth=None, random_state=42)
# tree3.fit(X_train, y_train)
# rules3 = export_text(tree3, feature_names=wine.feature_names)
# print("\n=== Reglas sin límite de profundidad ===")
# print(rules3[:1000])  # Mostramos solo las primeras líneas para no saturar
# print("Precisión (sin límite):", tree3.score(X_test, y_test))