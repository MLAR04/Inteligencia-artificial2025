# Árbol de Decisión con el Wine Dataset (scikit-learn)

## Descripción
Este proyecto utiliza el dataset clasico **Wine** de `scikit-learn` para entrenar un **clasificador simbolico basado en arboles de decisión**.  
El modelo genera **reglas lógicas interpretables** que permiten clasificar vinos en función de sus características químicas.

## Dataset: Wine
El dataset contiene **178 muestras de vino**, cada una con **13 características químicas** medidas en laboratorio, como:

- Alcohol  
- Ácido málico  
- Cenizas  
- Magnesio  
- Flavonoides  
- Proline (aminoácido relacionado con la uva)  

Las etiquetas (`target`) corresponden a **3 tipos de vino cultivados en la región italiana de Piamonte**:
- Clase 0  
- Clase 1  
- Clase 2  

## Objetivos
- Entrenar un árbol de decisión como **clasificador simbólico**.  
- Comprender cómo el modelo genera **reglas lógicas tipo si-entonces**.  
- Evaluar el desempeño del modelo en un conjunto de prueba.  


## Requisitos
Instalar las siguientes librerías de Python:

```bash
pip install scikit-learn numpy scipy