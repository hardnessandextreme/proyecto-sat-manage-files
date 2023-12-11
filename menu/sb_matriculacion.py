from funcionalidades.funcs import limpiar_pantalla

def registrar_matricula():
    try:
        limpiar_pantalla()
        alumno_id = input("Ingrese la identificación del alumno: ")
        materia_id = input("Ingrese la identificación de la materia: ")
        docente_id = input("Ingrese la identificación del docente: ")
        horario = input("Ingrese el horario (A, B o C): ")
        COSTO = input("Ingrese el costo de la materia: ")
        
        contenido_usuarios = open("datos/usuarios.txt", "r", encoding='utf-8')
        contenido_materias = open("datos/materias.txt", "r", encoding='utf-8')
        contenido_docentes = open("datos/docentes.txt", "r", encoding='utf-8')
        
        usuarios_data = contenido_usuarios.readlines()
        materias_data = contenido_materias.readlines()
        docentes_data = contenido_docentes.readlines()
        
        contenido_usuarios.close()
        contenido_materias.close()
        contenido_docentes.close()
        
        alumno_existe = False
        materia_existe = False
        docente_existe = False
        
        for line in usuarios_data:
            if line.split(',')[0] == alumno_id:
                alumno_existe = True
                break
        
        for line in materias_data:
            if line.split(',')[0] == materia_id:
                materia_existe = True
                break
        
        for line in docentes_data:
            if line.split(',')[0] == docente_id:
                docente_existe = True
                break
        
        if alumno_existe and materia_existe and docente_existe:
            alumno_name = ""
            alumno_apellido = ""
            for line in usuarios_data:
                if line.split(',')[0] == alumno_id:
                    alumno_name = line.split(',')[1]
                    alumno_apellido = line.split(',')[2]
                    break
            
            materia_name = ""
            for line in materias_data:
                if line.split(',')[0] == materia_id:
                    materia_name = line.split(',')[1]
                    break
            
            docente_name = ""
            docente_apellido = ""
            for line in docentes_data:
                if line.split(',')[0] == docente_id:
                    docente_name = line.split(',')[1]
                    docente_apellido = line.split(',')[2]
                    break
            
            confirm = input("\n¿Desea confirmar el registro? (S/N): ")
            
            if confirm.upper() == "S":
                matriculas_file = open("datos/matriculas.txt", "a", encoding='utf-8')
                matriculas_file.write(f"{alumno_name},{alumno_apellido},{materia_name},{docente_name},{docente_apellido},{horario},{COSTO}\n")
                matriculas_file.close()
                print("\nRegistro guardado exitosamente.")
                
            else:
                print("\nRegistro cancelado.")
                
        else:
            print("\nUno o más IDs no existen en los registros.")
        
        input('\nPresione una tecla para continuar...')


    except Exception as e:
        print(f'Error: {e}')
        input('\nPresione una tecla para continuar...')
        
def consultar_alumnos_matriculados():
    try:
        limpiar_pantalla()
        matriculas_file = open("datos/matriculas.txt", "r", encoding='utf-8')
        matriculas_data = matriculas_file.readlines()
        matriculas_file.close()
        
        print("Alumnos matriculados\n")
        
        lista = []
        
        for registro in matriculas_data:
            lista = registro.split(',')
            print(f'Estudiante: {lista[0]} {lista[1]}')
            print(f'Materia: {lista[2]}')
            print(f'Docente: {lista[3]} {lista[4]}')
            print(f'Horario: {lista[5]}')
            print(f'Costo: {lista[6]}')
        
        input('\nPresione una tecla para continuar...')
    except Exception as e:
        print(f'Error: {e}')
        input('\nPresione una tecla para continuar...')