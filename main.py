from menu.m_mantenimiento import menu_de_mantenimiento
from menu.m_matriculacion import menu_matriculacion
from menu.m_registronota import menu_registro_nota
from funcionalidades.funcs import *
import time

def menu_principal():
    ciclo= True
    while ciclo:
        limpiar_pantalla()
        print("Menu Principal\n")
        print("1. Mantenimiento\n"
              "2. Matriculacion\n"
              "3. Registro de notas\n"
              "4. Salir\n")
        
        try:
            verificar_carpeta_datos()
            opcion=int(input("Ingresa la opcion: "))

            if opcion == 1:
                menu_de_mantenimiento()
            elif opcion == 2:
                menu_matriculacion()
            elif opcion == 3:
                menu_registro_nota()
            elif opcion == 4:
                ciclo= False

        except Exception as e:
            print(f"\nError en el menu principal: {e}")
            input("\nPresione una tecla para continuar...")
            ciclo = False

if __name__=="__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print()
        print()
        print('Saliendo del programa...')
        time.sleep(1)
        exit()