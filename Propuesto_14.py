# propuesto14.py
import re
import os
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
habitaciones = [
    Habitacion(101, "Simple", 80),
    Habitacion(102, "Simple", 80),
    Habitacion(201, "Doble", 120),
    Habitacion(202, "Doble", 120),
    Habitacion(301, "Suite", 250),
]

ARCHIVO_RESERVAS = "reservas.txt"
def cargar_reservas():
    """Lee las reservas desde el archivo y devuelve lista."""
    if not os.path.exists(ARCHIVO_RESERVAS):
        return []
    with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as f:
        return [linea.strip().split("|") for linea in f.readlines()]

def guardar_reserva(cliente, num_hab, noches, total):
    """Guarda una nueva reserva en el archivo."""
    with open(ARCHIVO_RESERVAS, "a", encoding="utf-8") as f:
        f.write(f"{cliente}|{num_hab}|{noches}|{total}\n")

def habitacion_disponible(numero):
    """Verifica si una habitación ya está reservada."""
    reservas = cargar_reservas()
    for r in reservas:
        if str(numero) == r[1]:
            return False
    return True

def validar_nombre(nombre):
    """Valida que el nombre solo tenga letras y espacios."""
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{2,50}", nombre))

def validar_numero(valor):
    """Valida que el input sea un número entero."""
    return bool(re.fullmatch(r"\d+", valor))
def realizar_reserva():
    try:
        nombre = input("Ingrese nombre del cliente: ").strip()
        if not validar_nombre(nombre):
            raise ValueError(" Nombre inválido (solo letras y espacios, min 2 caracteres).")

        print("\n--- Habitaciones disponibles ---")
        for h in habitaciones:
            estado = "Disponible " if habitacion_disponible(h.numero) else "Ocupada "
            print(f"Habitación {h.numero} - {h.tipo} - S/ {h.precio} por noche - {estado}")

        num = input("\nIngrese número de habitación a reservar: ").strip()
        if not validar_numero(num):
            raise ValueError("Número de habitación inválido.")

        num = int(num)
        habitacion = next((h for h in habitaciones if h.numero == num), None)
        if not habitacion:
            raise LookupError(" La habitación no existe.")
        if not habitacion_disponible(num):
            raise Exception(" Habitación ya reservada.")
        noches = input("Ingrese cantidad de noches: ").strip()
        if not validar_numero(noches):
            raise ValueError(" Número de noches inválido.")
        noches = int(noches)
        total = habitacion.precio * noches
        guardar_reserva(nombre, num, noches, total)
        print(f"\n Reserva realizada con éxito para {nombre}. Total a pagar: S/ {total}\n")
    except Exception as e:
        print(e)
def verificar_disponibilidad():
    print("\n--- Disponibilidad de Habitaciones ---")
    for h in habitaciones:
        estado = "Disponible " if habitacion_disponible(h.numero) else "Ocupada "
        print(f"Habitación {h.numero} - {h.tipo} - S/ {h.precio} por noche - {estado}")
    print()

def generar_factura():
    try:
        cliente = input("Ingrese el nombre del cliente para generar factura: ").strip()
        if not validar_nombre(cliente):
            raise ValueError(" Nombre inválido.")

        reservas = cargar_reservas()
        facturas = [r for r in reservas if r[0].lower() == cliente.lower()]

        if not facturas:
            raise LookupError(" No se encontraron reservas para este cliente.")

        print("\n--- FACTURA ---")
        total_general = 0
        for r in facturas:
            _, num_hab, noches, total = r
            print(f"Habitación {num_hab} | Noches: {noches} | Subtotal: S/ {total}")
            total_general += int(total)
        print(f"TOTAL A PAGAR: S/ {total_general}\n")

    except Exception as e:
        print(e)
def menu():
    while True:
        print("=== SISTEMA DE RESERVAS HOTEL ===")
        print("1. Realizar Reserva")
        print("2. Verificar Disponibilidad")
        print("3. Generar Factura")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                realizar_reserva()
            elif opcion == "2":
                verificar_disponibilidad()
            elif opcion == "3":
                generar_factura()
            elif opcion == "4":
                print("👋 Saliendo del sistema...")
                break
            else:
                raise ValueError(" Opción inválida, intente nuevamente.")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    menu()
