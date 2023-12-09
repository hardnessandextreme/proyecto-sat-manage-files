from menu.sb_mantenimiento import *
from funcionalidades.funcs import limpiar_pantalla


def menu_de_mantenimiento():
   ciclo= True
   while ciclo:
      limpiar_pantalla()
      print("Menu Mantenimiento")
      print("1. Alumnos\n"
            "2. Materias\n"
            "3. Docentes\n"
            "4. Salir")
      
      try:
         opcion= int(input("Ingresa la opcion: "))

         if opcion == 1:
            print("Estoy en Alumnos")
            submenu_mantenimiento('Alumnos')
         elif opcion == 2:
            print("Estoy en Materias")
            submenu_mantenimiento('Materias')
         elif opcion == 3:
            print("Estoy en Docentes")
            submenu_mantenimiento('Docentes')
         elif opcion == 4:
            ciclo = False
         else:
            print('Ingrese una opción válida.')

      except Exception as e:
         pass

if __name__=="__main__":
    menu_de_mantenimiento()