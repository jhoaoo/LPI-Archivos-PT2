#Propuesto.15
import re
import os

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

ARCHIVO_PELICULAS = "peliculas.txt"


def cargar_peliculas():
    """Carga todas las películas desde el archivo."""
    if not os.path.exists(ARCHIVO_PELICULAS):
        return []
    with open(ARCHIVO_PELICULAS, "r", encoding="utf-8") as f:
        return [linea.strip().split("|") for linea in f.readlines()]

def guardar_pelicula(pelicula):
    """Guarda una nueva película en el archivo."""
    with open(ARCHIVO_PELICULAS, "a", encoding="utf-8") as f:
        f.write(f"{pelicula.titulo}|{pelicula.director}|{pelicula.anio}\n")

def validar_texto(cadena):
    """Valida que solo tenga letras, números, espacios y algunos signos básicos."""
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s\.,:;'\-]{2,100}", cadena))

def validar_anio(anio):
    """Valida que el año sea un número de 4 dígitos (1900–2100)."""
    return bool(re.fullmatch(r"(19\d{2}|20\d{2}|2100)", anio))

def agregar_pelicula():
    try:
        titulo = input("Ingrese título de la película: ").strip()
        if not validar_texto(titulo):
            raise ValueError("Título inválido (mínimo 2 caracteres, letras/números permitidos).")

        director = input("Ingrese director de la película: ").strip()
        if not validar_texto(director):
            raise ValueError(" Director inválido.")

        anio = input("Ingrese año de lanzamiento (1900–2100): ").strip()
        if not validar_anio(anio):
            raise ValueError(" Año inválido.")

        pelicula = Pelicula(titulo, director, anio)
        guardar_pelicula(pelicula)
        print(f"\nPelícula '{titulo}' registrada con éxito.\n")

    except Exception as e:
        print(e)

def buscar_pelicula():
    try:
        criterio = input("Buscar por (T)ítulo o (D)irector: ").strip().lower()
        if criterio not in ("t", "d"):
            raise ValueError("Opción inválida. Use T o D.")

        busqueda = input("Ingrese el texto de búsqueda: ").strip()
        if not validar_texto(busqueda):
            raise ValueError(" Texto de búsqueda inválido.")

        peliculas = cargar_peliculas()
        if not peliculas:
            print("No hay películas registradas.\n")
            return

        print("\n--- Resultados de Búsqueda ---")
        encontrados = []
        for p in peliculas:
            titulo, director, anio = p
            if (criterio == "t" and busqueda.lower() in titulo.lower()) or \
               (criterio == "d" and busqueda.lower() in director.lower()):
                print(f"Título: {titulo} | Director: {director} | Año: {anio}")
                encontrados.append(p)
        if not encontrados:
            print("No se encontraron coincidencias.\n")
        else:
            print()

    except Exception as e:
        print(e)

def listar_peliculas():
    peliculas = cargar_peliculas()
    if not peliculas:
        print("No hay películas registradas.\n")
        return

    print("\n--- LISTA DE PELÍCULAS ---")
    for p in peliculas:
        titulo, director, anio = p
        print(f"Título: {titulo} | Director: {director} | Año: {anio}")
    print()
def menu():
    while True:
        print("=== SISTEMA DE REGISTRO DE PELÍCULAS ===")
        print("1. Agregar película")
        print("2. Buscar película")
        print("3. Listar todas las películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                agregar_pelicula()
            elif opcion == "2":
                buscar_pelicula()
            elif opcion == "3":
                listar_peliculas()
            elif opcion == "4":
                print("👋 Saliendo del sistema...")
                break
            else:
                raise ValueError(" Opción inválida, intente nuevamente.")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    menu()
