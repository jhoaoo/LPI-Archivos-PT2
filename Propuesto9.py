def crear_archivo_texto():
    contenido = """aBc
Hola Mundo
Programar en Python es divertido
Python facilita el aprendizaje
"""
    with open("texto.txt", "w", encoding="utf-8") as f:
        f.write(contenido)
    print("Archivo 'texto.txt' creado con éxito.")
if __name__ == "__main__":
    crear_archivo_texto()

import re
import os
def contar_letras():
    archivo = input("Ingrese el nombre del archivo de texto: ").strip()
    if not os.path.exists(archivo):
        print("El archivo no existe.")
        return
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read().lower()  
    letras = re.findall(r"[a-z]", contenido)
    frecuencia = {}
    for letra in letras:
        frecuencia[letra] = frecuencia.get(letra, 0) + 1
    for letra in sorted(frecuencia.keys()):
        print(f"{letra} -> {frecuencia[letra]}")
if __name__ == "__main__":
    contar_letras()
