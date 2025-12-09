from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()
X, y = wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)

rules = export_text(tree, feature_names=wine.feature_names)
print("\nReglas del Árbol (max_depth=2)")
print(rules)

precision = tree.score(X_test, y_test)
print("\nPrecisión con max_depth=2:", precision)

tree_full = DecisionTreeClassifier(max_depth=None, random_state=42)
tree_full.fit(X_train, y_train)

rules_full = export_text(tree_full, feature_names=wine.feature_names)
print("\nReglas del Árbol Completo (max_depth=None)")
print(rules_full)

precision_full = tree_full.score(X_test, y_test)
print("\nPrecisión sin limite de profundidad:", precision_full)
