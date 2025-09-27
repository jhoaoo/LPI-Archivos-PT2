# crear_archivo_texto6.py
def crear_archivo_ejercicio6():
    nombre_archivo = "texto_ejercicio6.txt"
    contenido = "la vida es bella y la vida es hermosa"
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido + "\n")
        print(f"Archivo '{nombre_archivo}' creado con exito.")
    except Exception as e:
        print("Error al crear el archivo:", e)
if __name__ == "__main__":
    crear_archivo_ejercicio6()
#Ejercicio6.py
import re
import os
def contar_palabras_en_archivo(nombre_archivo):
    contador = {}
    try:
        if not os.path.isfile(nombre_archivo):
            raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe.")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = re.findall(r'\b\w+\b', linea.lower())
                for palabra in palabras:
                    contador[palabra] = contador.get(palabra, 0) + 1
        return contador
    except FileNotFoundError as fnf:
        print("Error:", fnf)
    except PermissionError:
        print("Error: No se tienen permisos para leer el archivo.")
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
    return None
def main():
    print(" Contador de palabras en archivo de texto\n")
    nombre_archivo = input("Ingrese el nombre del archivo (ej: texto.txt): ").strip()
    if not nombre_archivo.endswith('.txt'):
        print("Error: El archivo debe tener extension .txt")
        return
    conteo = contar_palabras_en_archivo(nombre_archivo)
    if conteo:
        print("\n Conteo de palabras:\n")
        for palabra in sorted(conteo):
            print(f"{palabra}: {conteo[palabra]}")
    else:
        print("No se pudo procesar el archivo.")
if __name__ == "__main__":
    main()

