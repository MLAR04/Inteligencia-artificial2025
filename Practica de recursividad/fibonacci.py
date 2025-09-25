def fibo(x):
    acumulador, suma = 0, 1
    fib = []
    while len(fib) < x:
        fib.append(acumulador)
        # Actualizamos ambos valores al mismo tiempo
        acumulador, suma = suma, acumulador + suma
    return fib

terminos = int(input("¿Cuántos términos de Fibonacci quieres?: "))
print(fibo(terminos))
