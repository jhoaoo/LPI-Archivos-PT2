import re
from pathlib import Path
from datetime import datetime
from pprint import pprint

ENTRADA = Path("directorio.txt")

RX_ID = re.compile(r"^\d+$")
RX_CEL = re.compile(r"^\d{9}$")
RX_FECHA = re.compile(r"^\d{2}/\d{2}/\d{4}$")

def parsear_linea(linea: str, nro_linea: int) -> dict:
    partes = [p.strip() for p in linea.split(";")]
    if len(partes) != 5:
        raise ValueError(f"Línea {nro_linea}: se esperaban 5 campos y llegaron {len(partes)}")

    id_str, nombre, apellido, celular, fecha = partes

    if not RX_ID.fullmatch(id_str):
        raise ValueError(f"Línea {nro_linea}: id no es entero ({id_str!r})")
    id_int = int(id_str)

    if not RX_CEL.fullmatch(celular):
        raise ValueError(f"Línea {nro_linea}: celular inválido ({celular!r}). Debe tener 9 dígitos.")

    if not RX_FECHA.fullmatch(fecha):
        raise ValueError(f"Línea {nro_linea}: fecha inválida ({fecha!r}). Formato DD/MM/YYYY.")
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        raise ValueError(f"Línea {nro_linea}: fecha inválida ({fecha!r}). Día/mes/año no válido.")

    return {
        "id": id_int,
        "nombre": nombre,
        "apellido": apellido,
        "celular": celular,
        "fecha de nacimiento": fecha,
    }

def leer_directorio(ruta: Path) -> list:
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo {ruta.name}. Asegúrese de crearlo en la misma carpeta del programa.")
    directorio = []
    with ruta.open("r", encoding="utf-8", errors="strict") as f:
        for idx, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                persona = parsear_linea(linea, idx)
                directorio.append(persona)
            except ValueError as e:
                print(f"Advertencia: {e}")
    return directorio

def main():
    try:
        lista = leer_directorio(ENTRADA)
        print("\nLista completa 'directorio':")
        pprint(lista, sort_dicts=False, width=100)
        print(f"\nTotal registros válidos: {len(lista)}")
    except FileNotFoundError as e:
        print(e)
    except UnicodeDecodeError:
        print("Error de codificación: el archivo debe estar en UTF-8.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()