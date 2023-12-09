from funcionalidades.funcs import limpiar_pantalla

def alta_ingreso(tipo):
    limpiar_pantalla()
    if tipo == 'Alumnos':
        try:
            archivo = open('datos/usuarios.txt', 'a', encoding='utf-8')
            archivo2 = open('datos/usuarios.txt', 'r', encoding='utf-8')

            print('Ingreso de datos\n')
            id_estudiante = int(input('Ingrese identificacion: '))

            # Validar si el ID ya existe en el archivo
            archivo2.seek(0)
            for linea in archivo2:
                lista = linea.split(',')
                if int(lista[0]) == id_estudiante:
                    print('\nError: El ID del estudiante ya existe en el archivo.')
                    archivo2.close()
                    return

            nombre_estudiante = input('Ingrese los nombres: ')
            apellido_estudiante = input('Ingrese los apellidos: ')
            edad_estudiante = int(input('Ingrese edad: '))
            cedula_estudiante = input('Ingrese la cedula: ')
            estado_estudiante = 1

            archivo.write(f'{id_estudiante},{nombre_estudiante},{apellido_estudiante},{edad_estudiante},{cedula_estudiante},{estado_estudiante}\n')
            print(f'\nDatos ingresados:\n'
                    f'ID: {id_estudiante}\n'
                    f'Nombre: {nombre_estudiante}\n'
                    f'Apellido: {apellido_estudiante}\n'
                    f'Edad: {edad_estudiante}\n'
                    f'Cedula: {cedula_estudiante}\n')
            
            
            archivo.close()

        except Exception as E:
          print(E)

    elif tipo == 'Materias':
        try:
            archivo = open('datos/materias.txt', 'a', encoding='utf-8')
            archivo2 = open('datos/materias.txt', 'r', encoding='utf-8')

            print(f'Ingreso de {tipo}\n')
            id_materia = int(input('Ingrese el ID de la materia: '))

            archivo2.seek(0)
            for linea in archivo2:
                lista = linea.split(',')
                if int(lista[0]) == id_materia:
                    print('Error: El ID de la materia ya existe en el archivo.')
                    archivo2.close()
                    return

            nombre_materia = input('Ingrese el nombre de la materia: ')
            numero_creditos = int(input('Ingrese el número de créditos: '))
            estado_materia = 1

            archivo.write(f'{id_materia},{nombre_materia},{numero_creditos},{estado_materia}\n')
            print(f'\nDatos ingresados:\n'
                  f'ID: {id_materia}\n'
                  f'Nombre materia: {nombre_materia}\n'
                  f'Número de créditos: {numero_creditos}\n')

            archivo.close()

        except Exception as E:
            print(f'Error al ingresar los datos: {E}\n')

    elif tipo == 'Docentes':
        try:
            archivo = open('datos/docentes.txt', 'a', encoding='utf-8')
            archivo2 = open('datos/docentes.txt', 'r', encoding='utf-8')

            print(f'Ingreso de {tipo}\n')
            id_docente = int(input('Ingrese el ID del docente: '))

            archivo2.seek(0)
            for linea in archivo2:
                lista = linea.split(',')
                if int(lista[0]) == id_docente:
                    print('Error: El ID del docente ya existe en el archivo.')
                    archivo2.close()
                    return

            nombre_docente = input('Ingrese los nombres del docente: ')
            apellido_docente = input('Ingrese los apellidos del docente: ')
            estado_docente = 1

            archivo.write(f'{id_docente},{nombre_docente},{apellido_docente},{estado_docente}\n')
            print(f'\nDatos ingresados:\n'
                  f'ID: {id_docente}\n'
                  f'Nombre docente: {nombre_docente}\n'
                  f'Apellido docente: {apellido_docente}\n')

            archivo.close()

        except Exception as E:
            print(f'Error al ingresar los datos: {E}\n')


def consultar_general(tipo):
    limpiar_pantalla()
    if tipo == 'Alumnos':
        try:
            print(f'Consulta General de {tipo}')
            archivo = open('datos/usuarios.txt', 'r', encoding='utf-8')

            activo = False
            lista = []
            lista_activos = []

            for linea in archivo:
                lista = linea.split(',')
                estado = lista[5].rstrip()

                if estado == '1':
                    activo = True
                    lista_activos.append(linea)

            if activo:
                for linea in lista_activos:
                    lista_activos = linea.split(',')
                    print(f'ID: {lista_activos[0]}')
                    print(f'Nombre: {lista_activos[1]}')
                    print(f'Apellido: {lista_activos[2]}')
                    print(f'Edad: {lista_activos[3]}')
                    print(f'Cedula: {lista_activos[4]}')
                    print()
            else:
                print('\nNo hay registros activos')

            archivo.close()

        except Exception as E:
            print(f'\nError al consultar los datos: {E}\n')
        
    elif tipo == 'Materias':
        try:
            print(f'Consulta General de {tipo}\n')
            archivo = open('datos/materias.txt', 'r', encoding='utf-8')

            activo = False
            lista = []
            lista_activos = []

            for linea in archivo:
                lista = linea.split(',')
                estado = lista[3].rstrip()

                if estado == '1':
                    activo = True
                    lista_activos.append(linea)

            if activo:
                for linea in lista_activos:
                    lista_activos = linea.split(',')
                    print(f'ID Materia: {lista_activos[0]}')
                    print(f'Nombre materia: {lista_activos[1]}')
                    print(f'Creditos: {lista_activos[2]}')
                    print()
            else:
                print('No hay registros activos')

            archivo.close()

        except Exception as E:
            print(f'Error al consultar los datos: {E}\n')
    
    elif tipo == 'Docentes':
        try:
            print(f'Consulta General de {tipo}\n')
            archivo = open('datos/docentes.txt', 'r', encoding='utf-8')

            activo = False
            lista = []
            lista_activos = []

            for linea in archivo:
                lista = linea.split(',')
                estado = int(lista[3].rstrip())

                if estado == 1:
                    activo = True
                    lista_activos.append(linea)

            if activo:
                for linea in lista_activos:
                    lista_activos = linea.split(',')
                    print(f'ID docente: {lista_activos[0]}')
                    print(f'Nombre docente: {lista_activos[1]}')
                    print(f'Apellido docente: {lista_activos[2]}')
                    print()
            else:
                print('No hay registros activos')

            archivo.close()

        except Exception as E:
            print(f'Error al consultar los datos: {E}\n')


def consultar_especifica(tipo, identificacion):
    limpiar_pantalla()
    if tipo == 'Alumnos':
        try:
            print('\nBusqueda de datos')

            archivo = open('datos/usuarios.txt', 'r', encoding='utf-8')
            
            info_est = []
            lista = []
            encontrado = False
            for linea in archivo:
                lista = linea.split(',')

                if str(identificacion) == lista[0]:
                    info_est.append(lista[0])
                    info_est.append(lista[1])
                    info_est.append(lista[2])
                    info_est.append(lista[3])
                    info_est.append(lista[4])
                    encontrado = True

            archivo.close()

            if encontrado:
                print(f'\nID: {info_est[0]}')
                print(f'Nombre: {info_est[1]}')
                print(f'Apellido: {info_est[2]}')
                print(f'Edad: {info_est[3]}')
                print(f'Cedula: {info_est[4]}')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al consultar el registro: {E}\n')
    
    elif tipo == 'Materias':
        try:
            print('\nBusqueda de datos')

            archivo = open('datos/materias.txt', 'r', encoding='utf-8')
            
            info_est = []
            lista = []
            encontrado = False
            for linea in archivo:
                lista = linea.split(',')

                if  str(identificacion) == lista[0]:
                    info_est.append(lista[0])
                    info_est.append(lista[1])
                    info_est.append(lista[2])
                    encontrado = True

            archivo.close()

            if encontrado:
                print(f'\nID: {info_est[0]}')
                print(f'Nombre materia: {info_est[1]}')
                print(f'Creditos: {info_est[2]}')

            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al consultar el registro: {E}\n')
    
    elif tipo == 'Docentes':
        try:
            print('\nBusqueda de datos')

            archivo = open('datos/docentes.txt', 'r', encoding='utf-8')
            
            info_est = []
            lista = []
            encontrado = False
            for linea in archivo:
                lista = linea.split(',')

                if  str(identificacion) == lista[0]:
                    info_est.append(lista[0])
                    info_est.append(lista[1])
                    info_est.append(lista[2])
                    encontrado = True

            archivo.close()

            if encontrado:
                print(f'\nID: {info_est[0]}')
                print(f'Nombres: {info_est[1]}')
                print(f'Apellidos: {info_est[2]}')

            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al consultar el registro: {E}\n')


def editar_registro(tipo, identificacion):
    limpiar_pantalla()
    if tipo == 'Alumnos':
        try:
            archivo = open('datos/usuarios.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    print(f'Edición de Registro de {tipo}\n')
                    nuevo_nombre = input('Ingrese el nuevo nombre: ')
                    nuevo_apellido = input('Ingrese el nuevo apellido: ')
                    nueva_edad = input('Ingrese la nueva edad: ')
                    nueva_cedula = input('Ingrese la nueva cedula: ')
                    estado = 1
                    lineas[i] = f'{identificacion},{nuevo_nombre},{nuevo_apellido},{nueva_edad},{nueva_cedula},{estado}\n'
                    break

            if encontrado:
                archivo = open('datos/usuarios.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('\nRegistro editado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al editar el registro: {E}')

    elif tipo == 'Materias':
        try:
            archivo = open('datos/materias.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    print(f'Edición de Registro de {tipo}\n')
                    nuevo_nombre_materia = input('Ingrese el nuevo nombre: ')
                    nuevo_credito = input('Ingrese el nuevo credito: ')
                    estado_materia = 1
                    lineas[i] = f'{identificacion},{nuevo_nombre_materia},{nuevo_credito},{estado_materia}\n'
                    break

            if encontrado:
                archivo = open('datos/materias.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('\nRegistro editado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al editar el registro: {E}')

    elif tipo == 'Docentes':
        try:
            archivo = open('datos/docentes.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    print(f'Edición de Registro de {tipo}')
                    nuevo_nombre_docente = input('Ingrese el nuevo nombre: ')
                    nuevo_apellido_docente = input('Ingrese el nuevo apellido: ')
                    estado_docente = 1
                    lineas[i] = f'{identificacion},{nuevo_nombre_docente},{nuevo_apellido_docente},{estado_docente}\n'
                    break

            if encontrado:
                archivo = open('datos/docentes.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('\nRegistro editado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al editar el registro: {E}')


def eliminar_registro(tipo, identificacion):
    limpiar_pantalla()
    if tipo == 'Alumnos':
        print(f'Eliminar Registro de {tipo}')
        try:
            archivo = open('datos/usuarios.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    lista[5] = '0\n'
                    lineas[i] = ','.join(lista)
                    break

            if encontrado:
                archivo = open('datos/usuarios.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('Registro eliminado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al eliminar el registro: {E}')

    elif tipo == 'Materias':
        print(f'Eliminar Registro de {tipo}')
        try:
            archivo = open('datos/materias.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    lista[3] = '0\n'
                    lineas[i] = ','.join(lista)
                    break

            if encontrado:
                archivo = open('datos/materias.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('Registro eliminado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al eliminar el registro: {E}')

    elif tipo == 'Docentes':
        print(f'Eliminar Registro de {tipo}')
        try:
            archivo = open('datos/docentes.txt', 'r', encoding='utf-8')
            lineas = archivo.readlines()
            archivo.close()

            encontrado = False
            for i in range(len(lineas)):
                lista = lineas[i].split(',')
                if str(identificacion) == lista[0]:
                    encontrado = True
                    lista[3] = '0\n'
                    lineas[i] = ','.join(lista)
                    break

            if encontrado:
                archivo = open('datos/docentes.txt', 'w', encoding='utf-8')
                archivo.writelines(lineas)
                archivo.close()
                print('Registro eliminado exitosamente')
            else:
                print('\nRegistro no encontrado')

        except Exception as E:
            print(f'Error al eliminar el registro: {E}')


if __name__ == '__main__':
    print('Funciones de la aplicación')
    identificacion = input('Ingrese identificacion: ')
    consultar_especifica('Alumnos', identificacion)
    # alta_ingreso('Alumnos')