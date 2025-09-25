# propuesto13.py
import re
import os
import csv
from datetime import datetime

class Gasto:
    def __init__(self, descripcion, monto, fecha, categoria):
        self.descripcion = descripcion
        self.monto = monto
        self.fecha = fecha
        self.categoria = categoria

ARCHIVO_GASTOS = "gastos.txt"

def cargar_gastos():
    if not os.path.exists(ARCHIVO_GASTOS):
        return []
    with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as f:
        return [linea.strip().split("|") for linea in f.readlines()]

def guardar_gasto(gasto):
    with open(ARCHIVO_GASTOS, "a", encoding="utf-8") as f:
        f.write(f"{gasto.descripcion}|{gasto.monto}|{gasto.fecha}|{gasto.categoria}\n")

def validar_texto(cadena):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\.,:;'\-]{2,100}", cadena))

def validar_monto(monto):
    return bool(re.fullmatch(r"\d+(\.\d{1,2})?", monto))

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def registrar_gasto():
    try:
        descripcion = input("Ingrese descripción del gasto: ").strip()
        if not validar_texto(descripcion):
            raise ValueError("Descripción inválida.")
        monto = input("Ingrese monto del gasto: ").strip()
        if not validar_monto(monto):
            raise ValueError("Monto inválido.")
        fecha = input("Ingrese fecha (YYYY-MM-DD): ").strip()
        if not validar_fecha(fecha):
            raise ValueError("Fecha inválida.")
        categoria = input("Ingrese categoría del gasto: ").strip()
        if not validar_texto(categoria):
            raise ValueError("Categoría inválida.")
        gasto = Gasto(descripcion, float(monto), fecha, categoria)
        guardar_gasto(gasto)
        print("Gasto registrado con éxito.\n")
    except Exception as e:
        print(e)

def resumen_gastos():
    try:
        gastos = cargar_gastos()
        if not gastos:
            print("No hay gastos registrados.\n")
            return
        resumen = {}
        for g in gastos:
            _, monto, fecha, categoria = g
            anio_mes = fecha[:7]
            clave = (anio_mes, categoria)
            resumen[clave] = resumen.get(clave, 0) + float(monto)
        print("\n--- Resumen de Gastos por Mes y Categoría ---")
        for clave, total in resumen.items():
            anio_mes, categoria = clave
            print(f"{anio_mes} | {categoria} | Total: {total:.2f}")
        print()
    except Exception as e:
        print(e)

def exportar_csv():
    try:
        gastos = cargar_gastos()
        if not gastos:
            print("No hay gastos registrados.\n")
            return
        with open("gastos.csv", "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Descripción", "Monto", "Fecha", "Categoría"])
            for g in gastos:
                escritor.writerow(g)
        print("Datos exportados a gastos.csv.\n")
    except Exception as e:
        print(e)

def menu():
    while True:
        print("=== CALCULADORA DE GASTOS PERSONALES ===")
        print("1. Registrar gasto")
        print("2. Ver resumen de gastos")
        print("3. Exportar datos a CSV")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                registrar_gasto()
            elif opcion == "2":
                resumen_gastos()
            elif opcion == "3":
                exportar_csv()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                raise ValueError("Opción inválida.")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    menu()
