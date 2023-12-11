import os
import os

def limpiar_pantalla():
    os.system('cls')

# def crear_archivos():
#     usuarios = open("datos/usuarios.txt", 'a', encoding='utf-8')
#     usuarios.close()
#     materias = open("datos/materias.txt", 'a', encoding='utf-8')
#     materias.close()
#     docentes = open("datos/docentes.txt", 'a', encoding='utf-8')
#     docentes.close()
#     matriculas = open("datos/matriculas.txt", 'a', encoding='utf-8')
#     matriculas.close()
#     notas = open("datos/notas.txt", 'a', encoding='utf-8')
#     notas.close()

def verificar_carpeta_datos():
    if not os.path.exists("datos"):
        os.makedirs("datos")
        usuarios = open("datos/usuarios.txt", 'a', encoding='utf-8')
        usuarios.close()
        materias = open("datos/materias.txt", 'a', encoding='utf-8')
        materias.close()
        docentes = open("datos/docentes.txt", 'a', encoding='utf-8')
        docentes.close()
        matriculas = open("datos/matriculas.txt", 'a', encoding='utf-8')
        matriculas.close()
        notas = open("datos/notas.txt", 'a', encoding='utf-8')
        notas.close()
