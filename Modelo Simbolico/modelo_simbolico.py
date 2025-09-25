# 1. Importar librerías necesarias
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# 2. Cargar el dataset del vino
wine = load_wine()
X, y = wine.data, wine.target

# 3. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Crear y entrenar el clasificador con profundidad limitada
tree_limited = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_limited.fit(X_train, y_train)

# 5. Exportar y visualizar las reglas simbólicas
print("=== ÁRBOL CON PROFUNDIDAD LIMITADA (max_depth=2) ===")
rules = export_text(tree_limited, feature_names=wine.feature_names)
print(rules)

# 6. Visualizar el árbol gráficamente
plt.figure(figsize=(12, 8))
plot_tree(tree_limited, feature_names=wine.feature_names,
          class_names=wine.target_names, filled=True, rounded=True)
plt.title("Árbol de Decisión - Profundidad Limitada (max_depth=2)")
plt.show()

# 7. Evaluar precisión del modelo limitado
y_pred_limited = tree_limited.predict(X_test)
accuracy_limited = accuracy_score(y_test, y_pred_limited)
print(f"Precisión con profundidad limitada: {accuracy_limited:.3f}")

# 8. Crear y entrenar clasificador sin limitación de profundidad
tree_full = DecisionTreeClassifier(max_depth=None, random_state=42)
tree_full.fit(X_train, y_train)

print("\n=== ÁRBOL SIN LIMITACIÓN DE PROFUNDIDAD ===")
rules_full = export_text(tree_full, feature_names=wine.feature_names)
print("Número de reglas/nodos:", len(rules_full.split('\n')))
print(f"Profundidad real del árbol: {tree_full.get_depth()}")

# 9. Evaluar precisión del modelo completo
y_pred_full = tree_full.predict(X_test)
accuracy_full = accuracy_score(y_test, y_pred_full)
print(f"Precisión sin limitación de profundidad: {accuracy_full:.3f}")

# 10. Comparar ambos modelos
print("\n=== COMPARACIÓN DE MODELOS ===")
print(f"Precisión modelo limitado (max_depth=2): {accuracy_limited:.3f}")
print(f"Precisión modelo completo (max_depth=None): {accuracy_full:.3f}")

# Reporte de clasificación detallado
print("\n=== REPORTE DE CLASIFICACIÓN (Modelo Completo) ===")
print(classification_report(y_test, y_pred_full, target_names=wine.target_names))
