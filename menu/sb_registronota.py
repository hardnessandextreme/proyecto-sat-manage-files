from funcionalidades.funcs import limpiar_pantalla

def registrar_calificaciones():
    limpiar_pantalla()
    print("Registro de calificaciones\n")
    try:
        id_alumno = int(input("Ingrese el id del alumno: "))
        id_materia = int(input("Ingrese el id de la materia: "))
        nota_1 = int(input("Ingrese la nota 1: "))
        nota_2 = int(input('Ingrese la nota 2: '))
        nota_3 = int(input('Ingrese la nota 3: '))
        nota_4 = int(input('Ingrese la nota 4: '))
        
        if nota_1 > 15 or nota_2 > 15:
            print("\nLa nota 1 y 2 no pueden ser mayor a 15\n")
            input("Presione enter para continuar...")
            return
        
        if nota_3 > 35 or nota_4 > 35:
            print("\nLa nota 3 y 4 no pueden ser mayor a 35\n")
            input("Presione enter para continuar...")
            return
        
        promedio = nota_1 + nota_2 + nota_3 + nota_4
        
        if promedio < 70:
            estado_materia = 'Reprobado'
        else:
            estado_materia = 'Aprobado'
        
        usuarios_file = open("datos/usuarios.txt", "r", encoding='utf-8')
        materias_file = open("datos/materias.txt", "r", encoding='utf-8')
        
        usuarios_data = usuarios_file.readlines()
        materias_data = materias_file.readlines()

        usuarios_file.close()
        materias_file.close()

        alumno_exists = False
        materia_exists = False
        
        for line in usuarios_data:
            if line.split(',')[0] == str(id_alumno):
                alumno_exists = True
                break
        
        for line in materias_data:
            if line.split(',')[0] == str(id_materia):
                materia_exists = True
                break
        
        if alumno_exists and materia_exists:
            alumno_name = ""
            alumno_apellido = ""
            for line in usuarios_data:
                if line.split(',')[0] == str(id_alumno):
                    alumno_name = line.split(',')[1]
                    alumno_apellido = line.split(',')[2]
                    break
            
            materia_name = ""
            for line in materias_data:
                if line.split(',')[0] == str(id_materia):
                    materia_name = line.split(',')[1]
                    break
                
            confirm = input("\n¿Desea confirmar el registro? (S/N): ")
            
            if confirm.upper() == "S":
                notas_contenido = open("datos/notas.txt", "a", encoding='utf-8')
                notas_contenido.write(f"{alumno_name},{alumno_apellido},{materia_name},{nota_1},{nota_2},{nota_3},{nota_4},{promedio},{estado_materia}\n")
                notas_contenido.close()
                print("\nRegistro guardado exitosamente.")
                
            else:
                print("\nRegistro cancelado.")
                
        else:
            print("\nUno o más IDs no existen en los registros.")
        
        input('\nPresione una tecla para continuar...')
        
    except Exception as e:
        print(f"\nError al registrar la calificacion {e}")
        input('\nPresione una tecla para continuar...')

def consultar_calificaciones():
    limpiar_pantalla()
    print("Consultar calificaciones\n")
    try:
        notas_contenido = open("datos/notas.txt", "r", encoding='utf-8')
        notas_data = notas_contenido.readlines()
        notas_contenido.close()
        
        if len(notas_data) == 0:
            print("No hay registro de calificaciones.")
            input('\nPresione una tecla para continuar...')
            return
        
        lista = []
        
        for registro in notas_data:
            lista = registro.split(',')
            print(f'Estudiante: {lista[0]} {lista[1]}')
            print(f'Materia: {lista[2]}')
            print('------------------------')
            print(f'Nota 1: {lista[3]}')
            print(f'Nota 2: {lista[4]}')
            print(f'Nota 3: {lista[5]}')
            print(f'Nota 4: {lista[6]}')
            print(f'Promedio: {lista[7]}')
            print(f'Estado: {lista[8].rstrip()}')
            print('------------------------\n')
        
        input('\nPresione una tecla para continuar...')
        
    except Exception as e:
        print(f"\nError al consultar la calificacion {e}")
        input("\nPresione enter para continuar...")
        