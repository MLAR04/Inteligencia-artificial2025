from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine() #cargar la base de datos
#wine.data es una matriz Numpy de 178 filas, 13 columnas
#wine.target un arreglo donde cada uno de sus elementos corresponde a cada una de las 178 filas
#que están en wine.data, representando la clase final del vino.
x, y = wine.data, wine.target

#Al asignar "0.2" en test_size, estamos reservando el otro 80% para entrenamiento
#a nuestro modelo con la información del dataset.
#random_state es simplemente una semilla para la reordenación aleatoria de todas las filas
#Asignarle un número como en este caso 18, garantiza que siempre que corramos el script 
#se desordenen de la misma forma.
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=18  
)

#Aquí apenas creamos el objeto arbol, aun no lo estamos entrenando. Estamos definiendo
#cuantos niveles de profundidad podrá "tener como máximo", más no significa que siempre
#llegue a ese nivel de profundidad. Incluso si no la limitamos (None), el arbol no crece
#tanto porque el algoritmo divide hasta donde es necesario, es decir, los nodos solo se
#crean cuando aportan información útil para clasificar, a eso sumemos que las muestras
#no son tantas (178)
tree = DecisionTreeClassifier(max_depth=8)

#Ahora si, entrenamos el arbol con los datos que usamos para el entrenamiento
tree.fit(x_train, y_train)

#Visualizamos el árbol de decisión ya entrenado.
rules = export_text(tree, feature_names=wine.feature_names)
print(rules)

#Vemos un porcentaje de la precisión que hubo en las predicciones con los datos
#que se utilizaron para prueba
print("Precisión en datos de prueba: ",tree.score(x_test,y_test))