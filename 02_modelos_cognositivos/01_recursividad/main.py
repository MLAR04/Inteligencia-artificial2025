def fib(n):
    if n == 0:
        return [1,1]
    lista = fib(n-1)
    lista.append(lista[-1] + lista[-2])
    return lista

def factorial(n):
    def f(x):
        if x == 1:
            return 1
        return x * f(x-1)

    def lista_nums(x):
        if x == 1:
            return [1]
        l = lista_nums(x-1)
        l.insert(0, x)
        return l

    return f(n), lista_nums(n)

print(fib(5))
print(factorial(7))
