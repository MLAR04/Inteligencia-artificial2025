import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
) 

digits = load_digits()
X = digits.data      
y = digits.target    

fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for ax, image, label in zip(axes.ravel(), digits.images[:10], y[:10]):
    ax.imshow(image, cmap="gray")
    ax.set_title(f"Digito: {label}")
    ax.axis("off")
plt.tight_layout()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

mlp = MLPClassifier(
    hidden_layer_sizes=(64, 32), 
    activation="relu",
    solver="adam",
    max_iter=300,
    random_state=42
)

mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"precision: {acc:.4f}\n")

print("Reporte de clasificacion:\n")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print("mtriz de confusioon:\n", cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=digits.target_names)
disp.plot(cmap="Blues")
plt.title("Matriz de confusion")
plt.show()