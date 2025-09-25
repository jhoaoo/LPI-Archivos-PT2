import re
from pathlib import Path
import sys

ARCHIVO = Path("contador.txt")
RX_INT = re.compile(r"^-?\d+$")

def leer_contador() -> int:
    if not ARCHIVO.exists() or ARCHIVO.stat().st_size == 0:
        ARCHIVO.write_text("0", encoding="utf-8", newline="\n")
        return 0
    try:
        contenido = ARCHIVO.read_text(encoding="utf-8").strip()
        if not RX_INT.fullmatch(contenido):
            raise ValueError("El archivo contiene un valor inválido.")
        return int(contenido)
    except (ValueError, OSError):
        ARCHIVO.write_text("0", encoding="utf-8", newline="\n")
        return 0

def escribir_contador(valor: int) -> None:
    tmp = ARCHIVO.with_suffix(".tmp")
    tmp.write_text(str(valor), encoding="utf-8", newline="\n")
    tmp.replace(ARCHIVO)

def main():
    try:
        accion = sys.argv[1].strip().lower() if len(sys.argv) > 1 else ""
        if accion not in {"", "inc", "dec"}:
            raise ValueError("Uso: propuesto3.py [inc|dec]")

        contador = leer_contador()
        if accion == "inc":
            contador += 1
        elif accion == "dec":
            contador -= 1

        print(contador)
        escribir_contador(contador)

    except PermissionError:
        print("Error: sin permisos para escribir/leer contador.txt")
    except OSError as e:
        print(f"Error de E/S: {e}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()