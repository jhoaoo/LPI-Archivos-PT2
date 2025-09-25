# propuesto12.py
import re
import os
from datetime import datetime

class Tarea:
    def __init__(self, descripcion, vencimiento, estado="Pendiente"):
        self.descripcion = descripcion
        self.vencimiento = vencimiento
        self.estado = estado

ARCHIVO_TAREAS = "tareas.txt"

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
        return [linea.strip().split("|") for linea in f.readlines()]

def guardar_tarea(tarea):
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as f:
        f.write(f"{tarea.descripcion}|{tarea.vencimiento}|{tarea.estado}\n")

def sobrescribir_tareas(lista):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        for t in lista:
            f.write("|".join(t) + "\n")

def validar_texto(cadena):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\.,:;'\-]{2,100}", cadena))

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def agregar_tarea():
    try:
        descripcion = input("Ingrese descripción de la tarea: ").strip()
        if not validar_texto(descripcion):
            raise ValueError("Descripción inválida.")
        vencimiento = input("Ingrese fecha de vencimiento (YYYY-MM-DD): ").strip()
        if not validar_fecha(vencimiento):
            raise ValueError("Fecha inválida.")
        tarea = Tarea(descripcion, vencimiento)
        guardar_tarea(tarea)
        print("Tarea registrada con éxito.\n")
    except Exception as e:
        print(e)

def marcar_completada():
    try:
        tareas = cargar_tareas()
        if not tareas:
            print("No hay tareas registradas.\n")
            return
        print("\n--- Tareas ---")
        for i, t in enumerate(tareas, start=1):
            print(f"{i}. {t[0]} | Vence: {t[1]} | Estado: {t[2]}")
        opcion = input("Seleccione el número de la tarea a completar: ").strip()
        if not opcion.isdigit() or not (1 <= int(opcion) <= len(tareas)):
            raise ValueError("Opción inválida.")
        idx = int(opcion) - 1
        tareas[idx][2] = "Completada"
        sobrescribir_tareas(tareas)
        print("Tarea marcada como completada.\n")
    except Exception as e:
        print(e)

def listar_pendientes():
    try:
        tareas = cargar_tareas()
        if not tareas:
            print("No hay tareas registradas.\n")
            return
        print("\n--- Tareas Pendientes ---")
        pendientes = [t for t in tareas if t[2] == "Pendiente"]
        if not pendientes:
            print("No hay tareas pendientes.\n")
        else:
            for t in pendientes:
                print(f"{t[0]} | Vence: {t[1]} | Estado: {t[2]}")
        print()
    except Exception as e:
        print(e)

def menu():
    while True:
        print("=== GESTOR DE TAREAS ===")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Listar tareas pendientes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                agregar_tarea()
            elif opcion == "2":
                marcar_completada()
            elif opcion == "3":
                listar_pendientes()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                raise ValueError("Opción inválida.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    menu()
