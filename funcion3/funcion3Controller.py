from funcion3.funcion3Model import decrementar_precio
import main

def fun3():
    
    print('''
            \n
            ===============================
            |         Funcion 3           |
            |-----------------------------|
            |   1. Decrecer Precio        |
            |   2. Volver al menú         |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            fun3_3()
        case "2":
            main.menuPrincipal()
        case _:
            print("Opción no válida")
            fun3()
            
            
def fun3_3():
    
    while True:
        try:
            modelo = int(input("Ingrese el modelo: "))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
            
    decrementar_precio(modelo)
    input("Presione una tecla para continuar")
    fun3()