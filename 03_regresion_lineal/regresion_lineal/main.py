import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

data = pd.read_csv("./articulos_ml.csv")

print("Dimensiones del dataset (filas, columnas):")
print(data.shape)          
print("\nPrimeros registros:")
print(data.head())

print("\nEstadísticas descriptivas:")
print(data.describe())

filtered_data = data[(data['Word count'] <= 3500) & (data['# Shares'] <= 80000)]
print("Dimensiones luego del filtrado:")
print(filtered_data.shape)

f1 = filtered_data['Word count'].values
f2 = filtered_data['# Shares'].values

media_palabras = 1808
colores = []
for _, row in filtered_data.iterrows():
    if row['Word count'] > media_palabras:
        colores.append('orange')  
    else:
        colores.append('blue')    

plt.figure()
plt.scatter(f1, f2, c=colores, s=40)
plt.xlabel("Word count")
plt.ylabel("# Shares")
plt.title("Relación entre cantidad de palabras y compartidos (# Shares)")
plt.show()



print("\n Regresion lineal una variable")

dataX = filtered_data[["Word count"]]
X_train = np.array(dataX)
y_train = filtered_data['# Shares'].values

regr = linear_model.LinearRegression()

regr.fit(X_train, y_train)

y_pred = regr.predict(X_train)

print("Coeficiente (pendiente m):", regr.coef_[0])
print("Termino independiente (b):", regr.intercept_)

print("Mean Squared Error (MSE): %.2f" % mean_squared_error(y_train, y_pred))
print("R^2 (Variance score): %.4f" % r2_score(y_train, y_pred))


print("\nEcuacion aproximada de la recta:")
print(f"   # Shares ≈ {regr.coef_[0]:.4f} * WordCount + {regr.intercept_:.2f}")

y_Dosmil = regr.predict([[2000]])
print("\n2000 palabras (solo usando Word count):")
print(f"   Shares ≈ {int(y_Dosmil.item())}")


plt.figure()
plt.scatter(X_train, y_train, color='blue', s=40, label="Datos reales")
plt.plot(X_train, y_pred, color='red', linewidth=2, label="Recta de regresión")
plt.xlabel("Word count")
plt.ylabel("# Shares")
plt.title("Regresion Lineal (1 variable): Word count vs # Shares")
plt.legend()
plt.show()


print("\n Regresion lineal multiples variables")

suma = (filtered_data["# of Links"] +
        filtered_data['# of comments'].fillna(0) +
        filtered_data['# Images video'])

dataX2 = pd.DataFrame()
dataX2["Word count"] = filtered_data["Word count"]
dataX2["suma"] = suma

XY_train = np.array(dataX2)
z_train = filtered_data['# Shares'].values

regr2 = linear_model.LinearRegression()

regr2.fit(XY_train, z_train)

z_pred = regr2.predict(XY_train)

print("Coeficientes (m1, m2):", regr2.coef_)
print("Termino independiente (b):", regr2.intercept_)
print("Mean Squared Error (MSE): %.2f" % mean_squared_error(z_train, z_pred))
print("R^2 (Variance score): %.4f" % r2_score(z_train, z_pred))

print("\nEcuacion aproximada del modelo con 2 variables:")
print(f"   # Shares ≈ {regr2.intercept_:.2f} "
      f"+ {regr2.coef_[0]:.4f} * WordCount "
      f"+ {regr2.coef_[1]:.4f} * (Links+Comments+Images)")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xx, yy = np.meshgrid(
    np.linspace(0, 3500, num=10),   
    np.linspace(0, 60, num=10)      
)

nuevoX = regr2.coef_[0] * xx
nuevoY = regr2.coef_[1] * yy
z = nuevoX + nuevoY + regr2.intercept_

ax.plot_surface(xx, yy, z, alpha=0.2, cmap=cm.hot)

ax.scatter(XY_train[:, 0], XY_train[:, 1], z_train,
           c='blue', s=30, label='Datos reales')

ax.scatter(XY_train[:, 0], XY_train[:, 1], z_pred,
           c='red', s=40, label='Predicción modelo')

ax.view_init(elev=30., azim=65)

ax.set_xlabel('Cantidad de Palabras')
ax.set_ylabel('Links + Comentarios + Imágenes')
ax.set_zlabel('Compartido (# Shares)')
ax.set_title('Regresión Lineal con Múltiples Variables')
ax.legend()

plt.show()



print("\n Prediccion con dos variables ")
ejemplo_suma = 10 + 4 + 6
z_Dosmil = regr2.predict([[2000, ejemplo_suma]])
print(f"Prediccion para 2000 palabras y suma={ejemplo_suma}:")
print(f"   Shares ≈ {int(z_Dosmil.item())}")

