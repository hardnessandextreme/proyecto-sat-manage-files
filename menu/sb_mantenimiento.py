from funcionalidades.sb_funcs import *
from funcionalidades.funcs import limpiar_pantalla

def submenu_mantenimiento(tipo):
   ciclo = True
   while ciclo:
      limpiar_pantalla()
      print(f'Submenu Mantenimiento {tipo}')
      print('1. Alta\n'
            '2. Consulta General\n'
            '3. Consulta Específica\n'
            '4. Edicion Registro\n'
            '5. Eliminar Registro\n'
            '6. Salir')
      
      try:
         opcion_submenu = int(input('Ingrese una opción: '))

         if opcion_submenu == 1:
            alta_ingreso(tipo)
         elif opcion_submenu == 2:
            consultar_general(tipo)
         elif opcion_submenu == 3:
            identificacion = int(input('Ingrese identificación: '))
            consultar_especifica(tipo, identificacion)
         elif opcion_submenu == 4:
            identificacion = int(input('Ingrese identificación: '))
            editar_registro(tipo, identificacion)
         elif opcion_submenu == 5:
            identificacion = int(input('Ingrese identificación: '))
            eliminar_registro(tipo, identificacion)
         elif opcion_submenu == 6:
            ciclo = False

         input('\nPresione una tecla para continuar...')
         limpiar_pantalla()

      except Exception as e:
         pass