import re
from pathlib import Path

VOCALES = set("aeiouáéíóúäëïöü")
SALIDA_OPCION1 = Path("vocales.txt")

RX_TEXTO = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$")
RX_OPCION = re.compile(r"^[123]$")

def contar_vocales(texto: str) -> dict:
    conteo = {v: 0 for v in "aeiou"}
    total = 0
    for ch in texto.lower():
        base = (
            "a" if ch in "aáä" else
            "e" if ch in "eéë" else
            "i" if ch in "iíï" else
            "o" if ch in "oóö" else
            "u" if ch in "uúü" else
            ""
        )
        if base:
            conteo[base] += 1
            total += 1
    conteo["total"] = total
    return conteo

def imprimir_conteo(conteo: dict) -> None:
    print("Conteo de vocales:")
    print(f"A: {conteo['a']}  E: {conteo['e']}  I: {conteo['i']}  O: {conteo['o']}  U: {conteo['u']}")
    print(f"Total: {conteo['total']}")

def escribir_reporte_vocales(conteo: dict, origen: str) -> None:
    lineas = [
        "===== Reporte de Vocales =====",
        f"Origen: {origen}",
        f"A: {conteo['a']}",
        f"E: {conteo['e']}",
        f"I: {conteo['i']}",
        f"O: {conteo['o']}",
        f"U: {conteo['u']}",
        f"Total: {conteo['total']}",
        ""
    ]
    tmp = SALIDA_OPCION1.with_suffix(".tmp")
    tmp.write_text("\n".join(lineas), encoding="utf-8", newline="\n")
    tmp.replace(SALIDA_OPCION1)
    print(f"Reporte guardado en: {SALIDA_OPCION1}")

def opcion_1():
    try:
        texto = input("Ingrese una oración: ").strip()
        if not texto or not RX_TEXTO.fullmatch(texto):
            raise ValueError("El texto debe contener solo letras y espacios.")
        conteo = contar_vocales(texto)
        imprimir_conteo(conteo)
        escribir_reporte_vocales(conteo, "Entrada por teclado")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
    except PermissionError:
        print("Error: sin permisos para escribir vocales.txt.")
    except OSError as e:
        print(f"Error de E/S: {e}")

def opcion_2():
    try:
        nombre = input("Ingrese el nombre del archivo (con extensión): ").strip()
        if not nombre:
            raise ValueError("Debe indicar un nombre de archivo.")
        ruta = Path(nombre)
        if not ruta.exists() or not ruta.is_file():
            raise FileNotFoundError(f"No se encontró el archivo: {nombre}")
        texto = ruta.read_text(encoding="utf-8", errors="replace")
        conteo = contar_vocales(texto)
        imprimir_conteo(conteo)
    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("Error: sin permisos para leer el archivo.")
    except UnicodeDecodeError:
        print("Error: no se pudo decodificar el archivo como UTF-8.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
    except OSError as e:
        print(f"Error de E/S: {e}")

def menu():
    while True:
        print("\n=== Menú ===")
        print("1. Leer cadena de caracteres")
        print("2. Leer archivo")
        print("3. Salir")
        opcion = input("Elija una opción (1-3): ").strip()
        if not RX_OPCION.fullmatch(opcion):
            print("Opción inválida. Intente nuevamente.")
            continue
        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            print("Programa terminado.")
            break

if __name__ == "__main__":
    menu()