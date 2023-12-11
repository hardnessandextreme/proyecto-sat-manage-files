from menu.sb_registronota import *

def menu_registro_nota():
    ciclo = True

    while ciclo:
        limpiar_pantalla()
        print("Menu Registro de Notas")
        print("1. Registro de calificaciones\n"
              "2. Consulta de calificaciones\n"
              "3. Salir")
        
        try:
            opcion= int(input("Ingresa la opcion: "))
            if opcion == 1:
                print("Estoy en registro de calificacion")
                registrar_calificaciones()
            elif opcion == 2:
                print("Estoy en Consulta de calificaciones")
                consultar_calificaciones()
            elif opcion == 3:
                ciclo = False
            else:
                print('Ingrese una opción válida.')
            
        except Exception as e:
            pass

if __name__=="__main__":
    menu_registro_nota()