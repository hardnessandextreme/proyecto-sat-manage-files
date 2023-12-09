def registrar_matricula():
    pass

def consultar_alumno_matriculado():
    pass


def menu_matriculacion():
    ciclo= True

    while ciclo:
        print("1. Registro de matricula\n"
              "2. Consulta de alumnos matriculados\n"
              "3. Salir")
        
        try:
            opcion= int(input("Ingresa la opcion: "))

            if opcion == 1:
                print("Estoy en Registro de matricula")
            elif opcion == 2:
                print("Estoy en Consulta de alumnos matriculados")
            elif opcion == 3:
                ciclo = False
            else:
                print('Ingrese una opción válida.')
                
        except Exception as e:
            pass

if __name__=="__main__":
    menu_matriculacion()