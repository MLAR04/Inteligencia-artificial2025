maestros ={
    "Roberto": ["Matematicas","Fisica"],
    "Mario": ["Quimica","Biologia"],
    "Diego":["Historia","Geografia"],
    "Laura":[]
}




alumnos={
    "Sofia":{"creditos":500,"materias":["Matematicas","Biologia", "Fisica", "Historia"], "servicioSocial": False, "practicas":True, "ingles":False},
    "Maria":{"creditos":495,"materias":["Geografia","Fisica"], "servicioSocial": True,"practicas":False, "ingles": False},
    "Ana":{"creditos":400,"materias":["Fisica"], "servicioSocial": False, "practicas":True, "ingles":False},
    "Luisa":{"creditos":500,"materias":["Biologia","Historia"], "servicioSocial": True, "practicas":True, "ingles":True}
}
   
def esta_maestro_activo(nombre_maestro):
    if nombre_maestro in maestros:
        if len(maestros[nombre_maestro]) != 0:
            print("Esta activo")
            return True
        else:
            print("no esta activo")
            return False
    else:
        print("No es un maestro")
        return
 
def puede_graduarse(nombre_alumno):
    if nombre_alumno in alumnos:
        alumno = alumnos[nombre_alumno]
        if alumno["creditos"] >= 500 and alumno["servicioSocial"] and alumno["practicas"] and alumno["ingles"]:
            print("El alumno puede graduarse")
            return True
        else:
            print("El alumno no puede graduarse")
            return False
    else:
        print("No es un alumno")
        return False


def cuantas_materias_lleva_alumno(nombre_alumno):
    if nombre_alumno in alumnos:
        alumno = alumnos[nombre_alumno]
        num_materias = len(alumno["materias"])
        print(f"El alumno lleva {num_materias} materias")
        return num_materias
    else:
        print("No es un alumno")
        return 0
   
def es_maestro(nombre_maestro):
    if nombre_maestro in maestros:
        print("Es un maestro")
        return True
    else:
        print("No es un maestro")
        return False


def es_alumno(nombre_alumno):
    if nombre_alumno in alumnos:
        print("Es un alumno")
        return True
    else:
        print("No es un alumno")
        return False


def creditos_para_graduarse(nombre_alumno):
    if nombre_alumno in alumnos:
        alumno = alumnos[nombre_alumno]
        creditos_necesarios = 500 - alumno["creditos"]
        if creditos_necesarios <= 0:
            print("El alumno ya tiene suficientes creditos para graduarse")
            return 0
        else:
            print(f"El alumno necesita {creditos_necesarios} creditos para graduarse")
            return creditos_necesarios
    else:
        print("No es un alumno")
        return None
   
def cantidad_materias_maestro(nombre_maestro):
    if nombre_maestro in maestros:
        materias = maestros[nombre_maestro]
        num_materias = len(materias)
        print(f"El maestro imparte {num_materias} materias")
        return num_materias
    else:
        print("No es un maestro")
        return 0


def es_alumno_de_maestro(nombre_maestro, nombre_alumno):
    if nombre_maestro in maestros and nombre_alumno in alumnos:
        materias_maestro = set(maestros[nombre_maestro])
        materias_alumno = set(alumnos[nombre_alumno]["materias"])
        if materias_maestro.intersection(materias_alumno):
            print(f"El alumno {nombre_alumno} es alumno del maestro {nombre_maestro}")
            return True
        else:
            print(f"El alumno {nombre_alumno} no es alumno del maestro {nombre_maestro}")
            return False
    else:
        print("No es un maestro o un alumno")
        return False
def comparten_misma_clase(nombre_alumno1, nombre_alumno2):
    if nombre_alumno1 in alumnos and nombre_alumno2 in alumnos:
        materias_alumno1 = set(alumnos[nombre_alumno1]["materias"])
        materias_alumno2 = set(alumnos[nombre_alumno2]["materias"])
        if materias_alumno1.intersection(materias_alumno2):
            print(f"Los alumnos {nombre_alumno1} y {nombre_alumno2} comparten al menos una clase")
            return True
        else:
            print(f"Los alumnos {nombre_alumno1} y {nombre_alumno2} no comparten ninguna clase")
            return False
    else:
        print("No es un alumno")
        return False


esta_maestro_activo("luis")
puede_graduarse("Luisa")
cuantas_materias_lleva_alumno("Sofia")
es_maestro("Laura")
es_alumno("Ana")
creditos_para_graduarse("Maria")
cantidad_materias_maestro("Roberto")
es_alumno_de_maestro("Roberto","Sofia")
