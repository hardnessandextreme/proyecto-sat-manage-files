def registrar_calificaciones():
    pass

def consultar_calificaciones():
    pass

def menu_registro_nota():
    ciclo = True

    while ciclo:
        print("1. Registro de calificaciones\n"
              "2. Consulta de calificaciones\n"
              "3. Salir")
        
        try:
            opcion= int(input("Ingresa la opcion: "))
            if opcion == 1:
                print("Estoy en registro de calificacion")
            elif opcion == 2:
                print("Estoy en Consulta de calificaciones")
            elif opcion == 3:
                ciclo = False
            else:
                print('Ingrese una opción válida.')
            
        except Exception as e:
            pass

if __name__=="__main__":
    menu_registro_nota()