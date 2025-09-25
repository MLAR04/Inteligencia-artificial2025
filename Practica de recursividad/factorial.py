def factorial(n):

    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Introduce un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
