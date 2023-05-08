from funcion1.funcion1Model import buscar_pc
import main

def fun1():
    
    print('''
            \n
            ===============================
            |         Funcion 1           |
            |-----------------------------|
            |   1. Buscar Modelo          |
            |   2. Volver al menú         |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            fun1_1()
        case "2":
            main.menuPrincipal()
        case _:
            print("Opción no válida")
            fun1()
            
            
def fun1_1():
    
    while True:
        try:
            velocidad = float(input("Ingrese la velocidad: "))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
            
    while True:
        try:
            tamaño = int(input("Ingrese el tamaño de la ram: "))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
            
    resultados = buscar_pc(velocidad, tamaño,)
    
    if not resultados:
        print("No se encontraron resultados")
        input("Presione una tecla para continuar")
        fun1()
    else:
        for pc in resultados:
            print("Modelo: ", pc['modelo'], " Precio: ", pc['precio'])
            input("Presione una tecla para continuar")
            fun1()