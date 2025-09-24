#Importamos las librerias necesarias de scikit-learn
from sklearn.datasets import load_wine #Dataset de vinos
from sklearn.tree import DecisionTreeClassifier, export_text #Arbol de decision y exportacion
from sklearn.model_selection import train_test_split #Division de datos en entramiento/prueba 

#Cargamos el dataset de vinos incluido en scikit-learn
wine = load_wine()
X, y = wine.data, wine.target #X: caracteristicas quimicas, y: clase (tipo de vino)

#Datos de entrenamiento 80%  y pruebas 20%
#random_state=42 asegura que la división sea siempre la misma
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)

#Creamos el clasificador arbol de decision
#max_depth limita la profundidad para que el arbol sea sencillo de intrepretar
tree = DecisionTreeClassifier (max_depth=2, random_state=42)

#Entrenamos el arbol con los datos de entrenamiento
tree.fit(X_train, y_train)

#Se exportan  las reglas aprendidas en formato de texto
rules = export_text(tree, feature_names=wine.feature_names)
print(rules) #Imprimir las reglas condicionales del arbol

#Se evalua el modelo en los datos de prueba y se muestra la precision
print ("Precisión en datos de prueba: ", tree.score(X_test, y_test))