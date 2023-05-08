from funcion4.funcion4Model import buscar_o_insertar_pc
import main

def fun4():
    
    print('''
            \n
            ===============================
            |         Funcion 4           |
            |-----------------------------|
            |   1. Buscar o Insertar Pc   |
            |   2. Volver al menú         |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            fun4_4()
        case "2":
            main.menuPrincipal()
        case _:
            print("Opción no válida")
            fun4()
            
            
def fun4_4():
    
    
    fabricante = input("Ingrese el fabricante: ")
            
    while True:
        try:
            modelo = int(input("Ingrese el modelo: "))
            break
        except ValueError:
            print("Error: El modelo debe ser un número entero")
            
    while True:
        try:
            velocidad = float(input("Ingrese la velocidad: "))
            break
        except ValueError:
            print("Error: La velocidad debe ser un número")
            
    while True:
        try:
            ram = int(input("Ingrese el tamaño de la RAM: "))
            break
        except ValueError:
            print("Error: El tamaño de la RAM debe ser un número entero")
            
    while True:
        try:
            disco = int(input("Ingrese el tamaño del disco duro: "))
            break
        except ValueError:  
            print("Error: El tamaño del disco duro debe ser un número entero")   
            
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número")
            
    buscar_o_insertar_pc(fabricante, modelo, velocidad, ram, disco, precio)
    input("Presione una tecla para continuar")
    fun4()
