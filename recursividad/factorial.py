def factorial(num):
    if num ==0 or num==1:
        return 1
    else:
        return num * factorial (num-1 )
        
num=int(input("El numero del factorial es: "))
print(factorial(num))