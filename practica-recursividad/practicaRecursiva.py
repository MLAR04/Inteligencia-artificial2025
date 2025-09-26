#20760257
#BUZO ZAMORA ELIAN
#Practica recursiva

def fibonacci(n):
    #estos son los casos bases (cuando se detiene la recursión)
    #si el valor de n es 1 o 2, devolvemos los primeros dos numeros
    # de la secuencia
    if n==1:
        return [1]       
    if n==2:
        return [1, 1]

    #hacemos la recursion hasta llegar al caso base
    arreglo=fibonacci(n-1)

    numero_anterior=arreglo[-1] #el largo de nuestro arreglo en la ultima posición (-1)
    numero_penultimo=arreglo[-2] #el largo del arreglo en la penultima posición (-2)

    #calculamos el valor siguiente y lo pusheamos al arreglo
    siguiente_numero=numero_anterior+numero_penultimo
    arreglo.append(siguiente_numero)

    return arreglo

#print(fibonacci(5)) #la sucesión para 5 numeros es [1, 1, 2, 3, 5]
########################################################################


def factorial(n):
    #caso base que n sea 1 (detener recursion)
    if n==1:
        return [1], 1

    #lo que se retorne de la función, lo asignamos en secuencia_anterior y valor_anterior
    secuencia_anterior, valor_anterior = factorial(n - 1)

    valor_actual= n*valor_anterior
    secuencia_anterior.append(n)

    return secuencia_anterior, valor_actual


secuencia,valor=factorial(7)
print(f"Factorial: {valor}, Secuencia: {secuencia}")
