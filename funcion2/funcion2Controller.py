
from funcion2.funcion2Model import eliminar_modelo
import main

def fun2():
    
    print('''
            \n
            ===============================
            |         Funcion 2           |
            |-----------------------------|
            |   1. Eliminar Modelo        |
            |   2. Volver al menú         |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            fun2_2()
        case "2":
            main.menuPrincipal()
        case _:
            print("Opción no válida")
            fun2()
            
            
def fun2_2():
    
    while True:
        try:
            modelo = int(input("Ingrese el modelo: "))
            break
        except ValueError:
            print("Oops! No era válido. Intente nuevamente...")
            
    eliminar_modelo(modelo)
    fun2()
        


