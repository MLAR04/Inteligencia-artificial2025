## Ricardo Haro Calvo
## alc17760295@ite.edu.mx
## Practica del modelo Conexionista

# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# Cargar la base de datos de dígitos
print("\nCargando datos de base de datos.")
digits = load_digits()
X = digits.data  # Características (imágenes de 8x8 aplanadas)
y = digits.target  # Etiquetas (0-9)

# Visualizar algunos ejemplos de dígitos
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='gray')
    ax.set_title(f'Etiqueta: {y[i]}')
    ax.axis('off')
plt.suptitle('Ejemplos de dígitos del dataset')
plt.tight_layout()
plt.show()

# Dividir los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nDatos de entrenamiento: {X_train.shape[0]} muestras")
print(f"Datos de prueba: {X_test.shape[0]} muestras")

# Crear el modelo de red neuronal multicapa
print("\nCreando modelo de red neuronal")
modelo = MLPClassifier(
    hidden_layer_sizes=(800, 400, 200),   # 2 capas ocultas con 100 y 50 neuronas
    activation='relu',              # Función de activación
    solver='adam',                  # Optimizador
    max_iter=500,                   # Número máximo de iteraciones
    random_state=42,                # Numero fijo para proceso aleatorio
    verbose=True                    # Mostrar progreso
)

# Entrenar la red neuronal
print("\nEntrenando la red neuronal")
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
print("\nRealizando predicciones")
y_pred = modelo.predict(X_test)

# Calcular la precisión
precision = accuracy_score(y_test, y_pred)
print('=================================================')
print(f"PRECISIÓN DEL MODELO: {precision * 100:.2f}%")
print('=================================================')

# Generar y visualizar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=range(10), yticklabels=range(10))
plt.title('Matriz de Confusión')
plt.ylabel('Etiqueta Real')
plt.xlabel('Etiqueta Predicha')
plt.show()
