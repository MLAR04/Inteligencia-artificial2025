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
    for padre in padres.values(): #usamos .values() porque "in" por sí solo verifica si hay una cadena dentro de otra. 
        if x in padre and y in padre:
            print(f"{x} y {y} son Hermanos");
            return True 
    print(f"{x} y {y} no son hermanos")
    return False 


def es_hijo_de(x,padre):
        if x in padres[padre]:
            print(f"{x} es hij@ de {padre}")
            return True
        else:
            print(f"{x} NO es hijo de ${padre}")
            return False


#quienes son los hijos de juan
def sus_hijos_son(padre):
    if padre in padres.keys():
         hijos=[]
         for elemento in padres[padre]:
              hijos.append(elemento)
         print(f"\nLos hijos de {padre} son: ")
         for elemento in hijos:
              print(elemento);

         return True;
    else:
         print("Ese padre no existe en el mapa")
         return False;


son_hermanos("Patricia","Esther");      
es_hijo_de("Patricia","Raul");
sus_hijos_son("Juan");
