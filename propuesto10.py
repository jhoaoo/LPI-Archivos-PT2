# propuesto10.py

class ArchivoError(Exception):
    """Clase base para excepciones relacionadas con el archivo."""
    pass

class ArchivoNoEncontradoError(ArchivoError):
    """Excepción para archivo no encontrado."""
    pass

class FormatoArchivoError(ArchivoError):
    """Excepción para errores de formato en el archivo."""
    pass


def leer_archivo(nombre_archivo):
    """Lee el archivo y devuelve un diccionario con los puntos por estudiante."""
    estudiantes = {}
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f, start=1):
                partes = linea.strip().split()
                if len(partes) != 3:
                    raise FormatoArchivoError(
                        f"Error en la línea {i}: formato incorrecto -> {linea.strip()}"
                    )
                nombre, apellido, puntos = partes
                try:
                    puntos = float(puntos)
                except ValueError:
                    raise FormatoArchivoError(
                        f"Error en la línea {i}: puntos no numéricos -> {puntos}"
                    )
                estudiante = f"{nombre} {apellido}"
                estudiantes[estudiante] = estudiantes.get(estudiante, 0) + puntos
        return estudiantes

    except FileNotFoundError:
        raise ArchivoNoEncontradoError(f"El archivo '{nombre_archivo}' no fue encontrado.")


def mostrar_reporte(estudiantes):
    """Muestra el reporte ordenado alfabéticamente."""
    if not estudiantes:
        print("No hay datos para mostrar.")
        return
    print("\n--- REPORTE DE PUNTOS ---")
    for estudiante in sorted(estudiantes.keys()):
        print(f"{estudiante}: {estudiantes[estudiante]} puntos")


def main():
    print("=== SISTEMA DE PUNTOS DE MARYSHECK ===")
    nombre_archivo = input("Ingrese el nombre del archivo (ejemplo: datos.txt): ").strip()

    try:
        estudiantes = leer_archivo(nombre_archivo)
        mostrar_reporte(estudiantes)

    except ArchivoNoEncontradoError as e:
        print("❌ Error:", e)
    except FormatoArchivoError as e:
        print("❌ Error de formato:", e)
    except ArchivoError as e:
        print("❌ Error general de archivo:", e)
    except Exception as e:
        print("❌ Error inesperado:", e)


if __name__ == "__main__":
    main()
