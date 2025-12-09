padres = {
    "Juan": ["Maria", "Carlos"],
    "Raul": ["Patricia", "Esther"]
}

def son_hermanos(x, y):
    son = any({x, y}.issubset(hijos) for hijos in padres.values())
    print("son hermanos" if son else "no son hermanos")
    return son

def su_papa_es(padre, hijo):
    return hijo in padres.get(padre, [])

def hijos_de(padre):
    return padres.get(padre, [])

son_hermanos("Patricia", "Esther")

if su_papa_es("Raul", "Maria"):
    print("Raul es padre de Maria")
else:
    print("raul nop es padre de Maria")

if su_papa_es("Juan", "Carlos"):
    print("Juan es padre de Carlos")
else:
    print("Juan no es padre de Carlos")

print(hijos_de("Juan"))
print(hijos_de("Raul"))
