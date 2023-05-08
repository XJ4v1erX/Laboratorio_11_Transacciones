from configuracion.config import connect
import funcion1.funcion1Controller
import funcion2.funcion2Controller
import funcion3.funcion3Controller
import funcion4.funcion4Controller



def menuPrincipal():
    
    print('''
            \n
            ===============================
            |         Menú principal      |
            |-----------------------------|
            |   1. Funcion 1              |
            |   2. Funcion 2              |
            |   3. Funcion 3              |
            |   4. Funcion 4              |
            |   5. Salir                  |
            |                             |
            ===============================
            ''')
    
    opcion = input("Ingrese una opción: ")
        
    match opcion:
        case "1":
            funcion1.funcion1Controller.fun1()
        case "2":
            funcion2.funcion2Controller.fun2()
        case "3":
            funcion3.funcion3Controller.fun3()
        case "4":
            funcion4.funcion4Controller.fun4()
        case "5":
            print("Gracias por usar el programa")
        case _:
            print("Opción no válida")
            menuPrincipal()
            
def main():
    connect()
    menuPrincipal()

if __name__ == '__main__':
    main()