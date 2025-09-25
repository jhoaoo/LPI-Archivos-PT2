# propuesto11.py
import re
import os

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

ARCHIVO_ESTUDIANTES = "estudiantes.txt"

def cargar_estudiantes():
    if not os.path.exists(ARCHIVO_ESTUDIANTES):
        return []
    with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as f:
        return [linea.strip().split("|") for linea in f.readlines()]

def guardar_estudiante(estudiante):
    calificaciones_str = ",".join(str(c) for c in estudiante.calificaciones)
    with open(ARCHIVO_ESTUDIANTES, "a", encoding="utf-8") as f:
        f.write(f"{estudiante.nombre}|{estudiante.edad}|{calificaciones_str}\n")

def validar_nombre(nombre):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,50}", nombre))

def validar_edad(edad):
    return bool(re.fullmatch(r"\d{1,2}", edad)) and 3 <= int(edad) <= 100

def validar_calificaciones(lista):
    try:
        calificaciones = [float(x) for x in lista]
        return all(0 <= c <= 20 for c in calificaciones)
    except ValueError:
        return False

def agregar_estudiante():
    try:
        nombre = input("Ingrese nombre del estudiante: ").strip()
        if not validar_nombre(nombre):
            raise ValueError("Nombre inválido.")
        edad = input("Ingrese edad del estudiante: ").strip()
        if not validar_edad(edad):
            raise ValueError("Edad inválida (3–100).")
        calificaciones_str = input("Ingrese calificaciones separadas por coma (ej: 15,18,12): ").strip().split(",")
        if not validar_calificaciones(calificaciones_str):
            raise ValueError("Calificaciones inválidas (solo números 0–20).")
        calificaciones = [float(x) for x in calificaciones_str]
        estudiante = Estudiante(nombre, int(edad), calificaciones)
        guardar_estudiante(estudiante)
        print("Estudiante registrado con éxito.\n")
    except Exception as e:
        print(e)

def listar_estudiantes():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    print("\n--- Lista de Estudiantes ---")
    for e in estudiantes:
        nombre, edad, calificaciones = e
        print(f"Nombre: {nombre} | Edad: {edad} | Calificaciones: {calificaciones}")
    print()

def promedio_estudiante():
    try:
        estudiantes = cargar_estudiantes()
        if not estudiantes:
            print("No hay estudiantes registrados.\n")
            return
        nombre_buscar = input("Ingrese el nombre del estudiante: ").strip()
        encontrado = None
        for e in estudiantes:
            nombre, edad, calificaciones = e
            if nombre.lower() == nombre_buscar.lower():
                calificaciones = [float(x) for x in calificaciones.split(",")]
                promedio = sum(calificaciones) / len(calificaciones)
                encontrado = (nombre, promedio)
                break
        if not encontrado:
            print("No se encontró el estudiante.\n")
        else:
            print(f"Promedio de {encontrado[0]}: {encontrado[1]:.2f}\n")
    except Exception as e:
        print(e)

def menu():
    while True:
        print("=== SISTEMA DE REGISTRO DE ESTUDIANTES ===")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Obtener promedio de un estudiante")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                agregar_estudiante()
            elif opcion == "2":
                listar_estudiantes()
            elif opcion == "3":
                promedio_estudiante()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                raise ValueError("Opción inválida.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    menu()
