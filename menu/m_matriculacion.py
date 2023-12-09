from menu.sb_matriculacion import *

def menu_matriculacion():
    ciclo = True

    while ciclo:
        limpiar_pantalla()
        print("1. Registro de matricula\n"
              "2. Consulta de alumnos matriculados\n"
              "3. Salir")
        
        try:
            opcion = int(input("Ingresa la opcion: "))

            if opcion == 1:
                registrar_matricula()
            elif opcion == 2:
                consultar_alumnos_matriculados()
            elif opcion == 3:
                ciclo = False
            else:
                print('Ingrese una opción válida.')
                
        except Exception as e:
            pass

if __name__ == "__main__":
    menu_matriculacion()