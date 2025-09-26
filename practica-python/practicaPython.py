#BUZO ZAMORA ELIAN
#02/09/2025
#Inteligencia Artificial

#Diccionario de "HECHOS". Cada padre tiene un arreglo de strings, que representa los hijos
#de cada padre.
padres={
    "Juan": ["Maria","Carlos"],
    "Raul": ["Patricia","Esther"]
}


def son_hermanos(x,y):
#for in por sí solo, verifica que un string exista dentro de otro string. En este caso
#buscamos que los strings que vamos a comparar, estén en alguno de los "values" del diccionario.
#Por eso usamos padres.values() en lugar de padres.
    for padre in padres.values(): #este ciclo itera cada value del diccionario.
        if x in padre and y in padre: #Verificamos que tanto "x" como "y" existan en el "value actual"
            print(f"{x} y {y} son Hermanos");
            return True #detenemos la función si se cumple la condición.
    print(f"{x} y {y} no son hermanos") #El flujo llega aquí si en ninguna de las iteraciones
    #se cumple la condición, por lo tanto no hay return y el flujo llega hasta aquí
    return False


def es_hijo_de(x,padre):
#Verificamos que "x" SÍ exista en el value de la key con el mismo nombre de "padre" en
#el diccionario
        if x in padres[padre]:
            print(f"{x} es hij@ de {padre}")
            return True
        else:
            print(f"{x} NO es hijo de ${padre}")
            return False



def sus_hijos_son(padre):
#Primero verificamos que "padre" exista en las keys del diccionario. Si existe, significa
#que tiene hijos y por tanto podemos iterarlo. 
    if padre in padres.keys():
         hijos=[] 
         for elemento in padres[padre]: #por cada hijo, lo metemos al arreglo hijos
              hijos.append(elemento)
         print(f"\nLos hijos de {padre} son: ")
         for elemento in hijos:
              print(elemento);

         return True;
    else:
         print("Ese padre no existe en el diccionario")
         return False;


son_hermanos("Patricia","Esther");      
es_hijo_de("Patricia","Raul");
sus_hijos_son("Raul");
