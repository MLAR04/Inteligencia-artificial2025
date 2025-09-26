padres ={
    "Juan": ["Maria", "Carlos"],
    "Raul": ["Patricia", "Esther"]
    
}

def son_hermanos (x, y):
    for hijos in padres.values():
         if x in hijos and y in hijos:
             print("son hermanos")
             return True
    print("no son hermanos")
    return False

def su_papa_es (nombre_padres, hijo):
        if nombre_padres in padres :
            if hijo in padres[nombre_padres]:
               return True
        return False
    
def hijos_de (padre):
    if padre in padres :
            return padres[padre]
    else:
        return[]
        

son_hermanos("Patricia", "Esther")

if su_papa_es("Raul", "Maria"):
    print("Raul es padre de Maria")
else:
    print("Raul no es padre de Maria")
    
    
if su_papa_es("Juan", "Carlos"):
    print("Juan es padre de Carlos")
else:
    print("Juan no es padre de Carlos")
    
print( hijos_de("Juan"))
print(hijos_de ("Raul"))
    

