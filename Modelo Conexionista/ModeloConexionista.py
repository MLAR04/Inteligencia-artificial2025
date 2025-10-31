import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar dataset de dígitos
digitos = load_digits()
imagenes_datos, etiquetas = digitos.data, digitos.target   # X = imagenes_datos, y = etiquetas

# Visualizar algunas imágenes con su número real
fig, ejes = plt.subplots(2, 5, figsize=(9, 4))
for eje, imagen, numero_real in zip(ejes.ravel(), digitos.images, digitos.target):
    eje.imshow(imagen, cmap='gray')
    eje.set_title(numero_real)
    eje.axis('off')
plt.show()

# Escalar y dividir en entrenamiento y prueba
escalador = StandardScaler()
imagenes_escaladas = escalador.fit_transform(imagenes_datos)

imagenes_entrenamiento, imagenes_prueba, etiquetas_entrenamiento, etiquetas_prueba = train_test_split(
    imagenes_escaladas, etiquetas, test_size=0.2, random_state=42, stratify=etiquetas
)

# Crear y entrenar el modelo de red neuronal
modelo_mlp = MLPClassifier(hidden_layer_sizes=(64,), max_iter=500, random_state=42)
modelo_mlp.fit(imagenes_entrenamiento, etiquetas_entrenamiento)

# Evaluar el modelo
predicciones = modelo_mlp.predict(imagenes_prueba)
precision = accuracy_score(etiquetas_prueba, predicciones)
matriz_confusion = confusion_matrix(etiquetas_prueba, predicciones)

print("Precisión del modelo:", precision)
print("Matriz de confusión:\n", matriz_confusion)



