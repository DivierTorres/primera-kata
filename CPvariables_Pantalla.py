"""
    Cambiar una palabra del archivo "fichero.txt" por otra palabra.


    fichero_leer = open("fichero.txt", "r") -> Abre el archivo en modo lectura.
    texto = fichero_leer.read() -> Lee el contenido del archivo.
    fichero_leer.close() -> Cierra el archivo.

    fichero_escribir = open("fichero.txt", "w") -> Abre el archivo en modo escritura.
    fichero_escribir.write() -> Escribe el contenido del archivo.
    fichero_escribir.close() -> Cierra el archivo.
"""
import sys

argumentos = sys.argv

archivo_txt = argumentos[1]
palabra_buscar = argumentos[2]
palabra_nueva = argumentos[3]

# Abrir archivo
# Leer el contenido del archivo y guardarlo en una variable (string)
# Cerrar archivo

# fichero_leer = open("fichero.txt", "r")
# texto = fichero_leer.read()
# fichero_leer.close()
with open('fichero.txt', 'r') as fichero:
    original = fichero.read()

# Buscar la palabra que quiero cambiar
# ¿debemos iterar?
# Sustituir la palabra por la nueva
# no necesito iterar, basta con usar .replace()
# https://docs.python.org/es/3/library/stdtypes.html#str.replace
nuevo_texto = original.replace(palabra_buscar, palabra_nueva)

# Abrir fichero
# Escribir el nuevo contenido (string)
# Cerrar fichero

# fichero_escribir = open("fichero.txt", "w")
# fichero_escribir.write(nuevo_texto)
# fichero_escribir.close()

with open('fichero.txt', 'w') as archivo:
    archivo.write(nuevo_texto)   


print('fichero.txt')