#Librerias
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier,plot_tree, export_text
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#cargo los datos del vino
wine = load_wine()
#x contiene las caracateristicas del vino, y la clase que es 0,1,2
x, y = wine.data, wine.target

x_train, x_test, y_train, y_test =train_test_split(x, y, test_size=0.2)

modelo= DecisionTreeClassifier(max_depth=None)
modelo.fit(x_train,y_train)



plt.figure(figsize=(12,6))
plot_tree(modelo, filled=True,
          feature_names=["alcohol","malic_acid","ash", "alcalinity_of_ash", "magnesium", "total_phenols", "flavanoids", "nonflavanoid_phenols", "proanthocyanins", "color_intensity", "hue", "od280/od315_of_diluted_wines", "proline"],
          class_names=["0", "1", "2"])
plt.show()

#exportar las reglas
rules=export_text(modelo, feature_names=["alcohol","malic_acid","ash", "alcalinity_of_ash", "magnesium", "total_phenols", "flavanoids", "nonflavanoid_phenols", "proanthocyanins", "color_intensity", "hue", "od280/od315_of_diluted_wines", "proline"])
print(rules)

print("Precisión en datos de prueba:", modelo.score(x_test, y_test))


#poder observar las caracteristicas del vino
#print(wine.feature_names)
