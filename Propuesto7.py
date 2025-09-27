#Crear archivo
def crear_archivo_ejemplo():
    nombre_archivo = "texto_ejercicio7.txt"
    contenido = "la vida es bella y la vida es hermosa"
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido + "\n")
        print(f"Archivo '{nombre_archivo}' creado correctamente con el contenido:")
        print(contenido)
    except Exception as e:
        print("Error al crear el archivo:", e)
if __name__ == "__main__":
    crear_archivo_ejemplo()

#Propuesto7.py
import os
import re
def contar_letras_en_archivo(nombre_archivo):
    contador = {}
    try:
        if not os.path.isfile(nombre_archivo):
            raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe.")
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                letras = re.findall(r'[a-zA-Z ]', linea)
                for letra in letras:
                    letra = letra.lower()  
                    contador[letra] = contador.get(letra, 0) + 1
        return contador
    except FileNotFoundError as fnf:
        print("Error:", fnf)
    except PermissionError:
        print("Error: No tiene permisos para leer el archivo.")
    except Exception as e:
        print("Error inesperado:", e)
    return None
def main():
    print(" Contador de letras en archivo de texto\n")
    nombre_archivo = input("Ingrese el nombre del archivo (ej: texto.txt): ").strip()
    if not nombre_archivo.endswith('.txt'):
        print("Error: El archivo debe tener extension .txt")
        return
    conteo = contar_letras_en_archivo(nombre_archivo)
    if conteo:
        print("\n Conteo de letras:\n")
        print(conteo)
    else:
        print("No se pudo procesar el archivo.")
if __name__ == "__main__":
    main()
