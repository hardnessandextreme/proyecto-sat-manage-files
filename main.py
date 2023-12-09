from menu.m_mantenimiento import menu_de_mantenimiento
from menu.m_matriculacion import menu_matriculacion
from menu.m_registronota import menu_registro_nota
from funcionalidades.funcs import limpiar_pantalla


def menu_principal():
    ciclo= True
    while ciclo:
        limpiar_pantalla()
        print("Menu Principal")
        print("1. Mantenimiento\n"
              "2. Matriculacion\n"
              "3. Registro de notas\n"
              "4. Salir")
        
        try:
            opcion=int(input("Ingresa la opcion: "))

            if opcion == 1:
                print("Estoy en matentenimiento")
                menu_de_mantenimiento()
            elif opcion == 2:
                print("Estoy en matriculacion")
                menu_matriculacion()
            elif opcion == 3:
                print("Estoy en Registro de notas")
                menu_registro_nota()
            elif opcion == 4:
                ciclo= False
            else:
                print('Ingrese una opción válida')

        except Exception as e:
            pass

if __name__=="__main__":
    menu_principal()