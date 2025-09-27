import os
import re
ARCHIVO = "agenda.txt"
def consultar_celular():
    nombre = input("Ingrese el nombre del cliente a consultar: ").strip()
    if not os.path.exists(ARCHIVO):
        print("La agenda no existe todavía.")
        return
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        contenido = f.read()
    patron = rf"^{re.escape(nombre)}:\s*(\d+)$"
    coincidencia = re.search(patron, contenido, re.MULTILINE | re.IGNORECASE)
    if coincidencia:
        print(f"El celular de {nombre} es: {coincidencia.group(1)}")
    else:
        print("El cliente no existe en la agenda.")
def anadir_celular():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    celular = input("Ingrese el número de celular: ").strip()
    if not re.fullmatch(r"\d{6,15}", celular):
        print("Número inválido. Debe contener solo dígitos (6 a 15).")
        return
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre}:{celular}\n")
    print(f"Cliente {nombre} añadido con éxito.")
def eliminar_celular():
    nombre = input("Ingrese el nombre del cliente a eliminar: ").strip()
    if not os.path.exists(ARCHIVO):
        print("La agenda no existe todavía.")
        return
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    patron = rf"^{re.escape(nombre)}:.*$"
    nuevo_contenido = [linea for linea in lineas if not re.match(patron, linea, re.IGNORECASE)]
    if len(lineas) == len(nuevo_contenido):
        print("El cliente no existe en la agenda.")
    else:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.writelines(nuevo_contenido)
        print(f"Cliente {nombre} eliminado correctamente.")
def crear_agenda():
    if os.path.exists(ARCHIVO):
        opcion = input("La agenda ya existe. ¿Desea sobrescribirla? (s/n): ").strip().lower()
        if opcion != "s":
            print("Operación cancelada.")
            return
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        pass 
    print("Agenda creada exitosamente.")
def menu():
    while True:
        print("\n--- AGENDA TELEFÓNICA ---")
        print("1. Consultar un celular")
        print("2. Añadir un celular")
        print("3. Eliminar un celular")
        print("4. Crear la agenda")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip() 
        if opcion == "1":
            consultar_celular()
        elif opcion == "2":
            anadir_celular()
        elif opcion == "3":
            eliminar_celular()
        elif opcion == "4":
            crear_agenda()
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción inválida, intente nuevamente.")
if __name__ == "__main__":
    menu()
