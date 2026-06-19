from fn import * 
while True:
    menu()
    opcion = validar_num("Selecciona una opción del menú: ")
    archivo = "paises.csv"
    match opcion:
        case 1 | "1":
            cargar_pais(archivo)
        case 2 | "2":
            actualizar_pais(archivo)
        case 3 | "3":
            pass
        case 4 | "4":
            filtar_paises(archivo)
        case 5 | "5":
            ordenar_paises(archivo)
        case 6 | "6":
            pass
        case 7 | "7":
            print("Gracias por usar el sistema!")
            break
        case _:
            print("Ingresa un número del menú")
    