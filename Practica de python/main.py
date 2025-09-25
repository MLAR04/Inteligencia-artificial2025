# Base de conocimiento - Hechos
hechos = {
    'padre': [
        ('juan', 'maria'),
        ('juan', 'carlos')
    ]
}

# Funciones de consulta
def es_padre_de(padre, hijo):
    """Consulta si alguien es padre de otro"""
    return (padre, hijo) in hechos['padre']

def hijos_de(padre):
    """Obtiene todos los hijos de una persona"""
    return [hijo for (p, hijo) in hechos['padre'] if p == padre]

def padres_de(hijo):
    """Obtiene todos los padres de una persona"""
    return [padre for (padre, h) in hechos['padre'] if h == hijo]

# Consultas
print("=== CONSULTAS ===")
print("¿Juan es padre de María?", es_padre_de('juan', 'maria'))
print("¿Juan es padre de Carlos?", es_padre_de('juan', 'carlos'))
print("Hijos de Juan:", hijos_de('juan'))
print("Padres de María:", padres_de('maria'))
