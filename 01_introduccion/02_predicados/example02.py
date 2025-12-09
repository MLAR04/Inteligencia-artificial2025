maestros = {
    "Roberto": ["Matematicas", "Fisica"],
    "Mario": ["Quimica", "Biologia"],
    "Diego": ["Historia", "Geografia"],
    "Laura": []
}
alumnos = {
    "Sofia": {
        "creditos": 500,
        "materias": ["Matematicas", "Biologia", "Fisica", "Historia"],
        "servicioSocial": False,
        "practicas": True,
        "ingles": False
    },
    "Maria": {
        "creditos": 495,
        "materias": ["Geografia", "Fisica"],
        "servicioSocial": True,
        "practicas": False,
        "ingles": False
    },
    "Ana": {
        "creditos": 400,
        "materias": ["Fisica"],
        "servicioSocial": False,
        "practicas": True,
        "ingles": False
    },
    "Luisa": {
        "creditos": 500,
        "materias": ["Biologia", "Historia"],
        "servicioSocial": True,
        "practicas": True,
        "ingles": True
    }
}

def esta_maestro_activo(nombre_maestro):
    materias = maestros.get(nombre_maestro)
    if materias is None:
        print("No es un maestro")
        return False

    activo = bool(materias)
    print("Esta activo" if activo else "no esta activo")
    return activo


def puede_graduarse(nombre_alumno):
    alumno = alumnos.get(nombre_alumno)
    if alumno is None:
        print("No es un alumno")
        return False

    cumple = (
        alumno["creditos"] >= 500
        and alumno["servicioSocial"]
        and alumno["practicas"]
        and alumno["ingles"]
    )

    print("El alumno puede graduarse" if cumple else "El alumno no puede graduarse")
    return cumple


def cuantas_materias_lleva_alumno(nombre_alumno):
    alumno = alumnos.get(nombre_alumno)
    if alumno is None:
        print("No es un alumno")
        return 0

    num_materias = len(alumno["materias"])
    print(f"El alumno lleva {num_materias} materias")
    return num_materias


def es_maestro(nombre_maestro):
    es = nombre_maestro in maestros
    print("Es un maestro" if es else "No es un maestro")
    return es


def es_alumno(nombre_alumno):
    es = nombre_alumno in alumnos
    print("Es un alumno" if es else "No es un alumno")
    return es


def creditos_para_graduarse(nombre_alumno):
    alumno = alumnos.get(nombre_alumno)
    if alumno is None:
        print("No es un alumno")
        return None

    faltan = max(0, 500 - alumno["creditos"])
    if faltan == 0:
        print("El alumno ya tiene suficientes creditos para graduarse")
    else:
        print(f"El alumno necesita {faltan} creditos para graduarse")
    return faltan


def cantidad_materias_maestro(nombre_maestro):
    materias = maestros.get(nombre_maestro)
    if materias is None:
        print("No es un maestro")
        return 0

    num_materias = len(materias)
    print(f"El maestro imparte {num_materias} materias")
    return num_materias


def es_alumno_de_maestro(nombre_maestro, nombre_alumno):
    materias_maestro = maestros.get(nombre_maestro)
    alumno = alumnos.get(nombre_alumno)

    if materias_maestro is None or alumno is None:
        print("No es un maestro o un alumno")
        return False

    comparte = bool(set(materias_maestro) & set(alumno["materias"]))
    if comparte:
        print(f"El alumno {nombre_alumno} es alumno del maestro {nombre_maestro}")
    else:
        print(f"El alumno {nombre_alumno} no es alumno del maestro {nombre_maestro}")
    return comparte


def comparten_misma_clase(nombre_alumno1, nombre_alumno2):
    a1 = alumnos.get(nombre_alumno1)
    a2 = alumnos.get(nombre_alumno2)

    if a1 is None or a2 is None:
        print("No es un alumno")
        return False

    comparten = bool(set(a1["materias"]) & set(a2["materias"]))
    if comparten:
        print(f"Los alumnos {nombre_alumno1} y {nombre_alumno2} comparten al menos una clase")
    else:
        print(f"Los alumnos {nombre_alumno1} y {nombre_alumno2} no comparten ninguna clase")
    return comparten


esta_maestro_activo("luis")
puede_graduarse("Luisa")
cuantas_materias_lleva_alumno("Sofia")
es_maestro("Laura")
es_alumno("Ana")
creditos_para_graduarse("Maria")
cantidad_materias_maestro("Roberto")
es_alumno_de_maestro("Roberto", "Sofia")
