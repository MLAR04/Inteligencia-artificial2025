## Practica SciKitLearn Conexionista

# Paso 1. Importar librerías necesarias. Además de numpy, matplotlib, y scikitlearn, utilizaremos seaborn para mejor visualizar los resultados de nuestra red neuronal.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

# Paso 2. Cargar la base de datos de dígitos

digits = load_digits()
X = digits.data  # Características (imágenes de 8x8 aplanadas)
y = digits.target  # Etiquetas (0-9)

# Paso 3 (Opcional). Visualizar algunos ejemplos de los datos cargados.

fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
   ax.imshow(digits.images[i], cmap='gray')
   ax.set_title(f'Etiqueta: {y[i]}')
   ax.axis('off')
plt.suptitle('Ejemplos de dígitos del dataset')
plt.tight_layout()
plt.show()

# Paso 4. Dividir los datos entre datos de prueba y datos de entrenamiento.

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.2, random_state=42, stratify=y
)

# Paso 5. Crear el modelo de red neuronal multicapa.

modelo = MLPClassifier(
   hidden_layer_sizes=(100, 50),  # 2 capas ocultas con 100 y 50 neuronas
   activation='relu',              # Función de activación
   solver='adam',                  # Optimizador
   max_iter=500,                   # Número máximo de iteraciones
   random_state=42,		     # Número fijo para proceso aleatorio
   verbose=True                    # Mostrar progreso
)

# Paso 6. Entrenar la red neuronal con los datos ya separados.

modelo.fit(X_train, y_train)

# Paso 7. Realizar predicciones sobre el modelo para contrastar despues

y_pred = modelo.predict(X_test)

# Paso 8. Calcular la precisión del modelo.

precision = accuracy_score(y_test, y_pred)
print(f"PRECISIÓN DEL MODELO: {precision * 100:.2f}%")

# Paso 9. Generar y visualizar matriz de confusión 

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
           xticklabels=range(10), yticklabels=range(10))
plt.title('Matriz de Confusión')
plt.ylabel('Etiqueta Real')
plt.xlabel('Etiqueta Predicha')
plt.show()


## Preguntas de reflexión

# ¿Qué tan preciso fue el modelo?
El modelo presentó una precisión de 97.78% a lo largo de 101 iteraciones con la configuración mostrada en esta práctica

# ¿Dónde se equivocó más?
De acuerdo con la matriz de confusión, el modelo presentó la mayor cantidad de fallas clasificando los números “8” como “1”

# ¿Cómo cambian los resultados si modificas el número de capas y neuronas?
Entrenando 2 modelos nuevos, (1) uno con aproximadamente ¼ de neuronas (25, 15) y otro (2) con más capas y el más del doble de neuronas (800, 400, 200) ,observamos los siguientes resultados.
El modelo (1) logró una precisión del 96.67%, el cual logró a través de 252 iteraciones, observando la matriz de confusión, este tendió a equivocarse en las mismas áreas que el modelo base.

El modelo (2) logró una precisión del 96.67%, el cual logró a través de 30 iteraciones, observando la matriz de confusión, de manera notable, este modelo se equivoca en las mismas áreas que el modelo (1) y el modelo base.

Referencias
Matplotlib. (2024). Matplotlib: Python plotting — Matplotlib 3.3.4 documentation. Matplotlib.org. https://matplotlib.org/stable/index.html
scikit-learn. (2010). sklearn.neural_network.MLPClassifier — scikit-learn 0.20.3 documentation. Scikit-Learn.org. https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
seaborn. (n.d.). An introduction to seaborn — seaborn 0.12.0 documentation. Seaborn.pydata.org. https://seaborn.pydata.org/tutorial/introduction
sklearn. (n.d.). sklearn.datasets.load_digits. Scikit-Learn. https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

