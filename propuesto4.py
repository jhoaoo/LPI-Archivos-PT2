import re
from pathlib import Path

def contar_palabras_y_coincidencias(ruta: Path, objetivo: str) -> tuple[int, int]:
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    tokens = re.findall(r"\b\w+\b", texto.lower(), flags=re.UNICODE)
    total = len(tokens)
    coincidencias = sum(1 for t in tokens if t == objetivo.lower())
    return total, coincidencias

def main():
    try:
        nombre = input("Ingrese el nombre del archivo (con extensión): ").strip()
        if not nombre:
            raise ValueError("Debe indicar un nombre de archivo.")
        palabra = input("Ingrese la palabra a buscar: ").strip()
        if not palabra:
            raise ValueError("Debe indicar la palabra a buscar.")

        ruta = Path(nombre)
        if not ruta.exists() or not ruta.is_file():
            raise FileNotFoundError(f"No se encontró el archivo: {nombre}")

        total, matches = contar_palabras_y_coincidencias(ruta, palabra)
        print(f"Total de palabras en el archivo: {total}")
        print(f"Coincidencias de '{palabra}': {matches}")

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

if __name__ == "__main__":
    main()