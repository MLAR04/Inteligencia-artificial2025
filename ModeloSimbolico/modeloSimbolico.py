from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()
data, target = wine.data,wine.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=2)
model.fit(X_train, y_train)

rules = export_text(model, feature_names=wine.feature_names)
print(rules)

print("Accuracy: ", model.score(X_test, y_test))