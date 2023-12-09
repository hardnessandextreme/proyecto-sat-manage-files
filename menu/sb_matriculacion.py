from funcionalidades.funcs import limpiar_pantalla

def registrar_matricula():
    limpiar_pantalla()
    alumno_id = input("Ingrese la identificación del alumno: ")
    materia_id = input("Ingrese la identificación de la materia: ")
    docente_id = input("Ingrese la identificación del docente: ")
    horario = input("Ingrese el horario (A, B o C): ")
    COSTO = input("Ingrese el costo de la materia: ")
    
    usuarios_file = open("datos/usuarios.txt", "r", encoding='utf-8')
    materias_file = open("datos/materias.txt", "r", encoding='utf-8')
    docentes_file = open("datos/docentes.txt", "r", encoding='utf-8')
    
    usuarios_data = usuarios_file.readlines()
    materias_data = materias_file.readlines()
    docentes_data = docentes_file.readlines()
    
    usuarios_file.close()
    materias_file.close()
    docentes_file.close()
    
    alumno_exists = False
    materia_exists = False
    docente_exists = False
    
    for line in usuarios_data:
        if line.split(',')[0] == alumno_id:
            alumno_exists = True
            break
    
    for line in materias_data:
        if line.split(',')[0] == materia_id:
            materia_exists = True
            break
    
    for line in docentes_data:
        if line.split(',')[0] == docente_id:
            docente_exists = True
            break
    
    if alumno_exists and materia_exists and docente_exists:
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

def consultar_alumnos_matriculados():
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