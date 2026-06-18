import csv
def menu():
    print('''
    1) Agregar país
    2) Actualizar datos de un país
    3) Buscar pais
    4) Filtrar países
    5) Ordenar paises 
    6) Mostrar estadísticas
    7) Salir 
    ''')

def validar_num(valor): #Función validadora de la opción del menú (que sea un número > 0)
    while True:
        try:
            num = int(input(valor))
            if num >0:
                return num
            else:
                print("ERROR: Ingresa un número positivo \n")
        except ValueError:
            print("ERROR: Ingresa un número \n")

def validar_str(mensaje): #Función validadora de strings (verifica que el nómbre sea válido)
    while True: 
        try:
            cadena = input(mensaje).strip().capitalize()
            if cadena.isalpha():
                return cadena
            else:
                print("ERROR - No puede ser vacío \n")
        except TypeError:
            print("ERROR - Ingresa solo texto \n")

def actualizar_pais(paises): #Función que recibe un país ingresado por el usuario, busca en el csv si existe y luego el usuario ingresa un nuevo valor de población y superficie
    buscado = validar_str("Qué país querés modificar?: ")
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        datos = list(lector)
        encabezados = lector.fieldnames
    for p in datos:
        if p["nombre"] == buscado:
            p["poblacion"] = validar_num("Ingresá la población actualiada: ")
            p["superficie"] = validar_num("Ingresa la superficie actualizada:")
    
    with open(paises, "r+", encoding = "utf-8", newline = "") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)
    for p in datos:
        if p["nombre"] == buscado:
            print(f"País actualizado - {buscado}  Población - {p['poblacion']}  Superficie - {p['superficie']}")

def filtar_paises (paises): #Función que agrupa 3 filtros distintos según el que quiera el usuario
    print("Filtros: Continente, Población o Superficie")
    opcion = validar_str("Qué filtro querés aplicar (Ingresa C, P o S)?: \n")
    match opcion:
        case "C":
            filtrar_x_continente(paises)
        case "P":
            filtrar_x_poblacion(paises)
        case "S":
            filtrar_x_superficie(paises)
        case _:
            print("ERROR - Ingresa un filtro válido")

def filtrar_x_continente(paises): #Función que  pide un continente y muestra todos los paises pertenecientes que estén ingresados 
    continente = validar_str("Qué continente querés mostrar?: ")
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        continentes = list(lector)
    if any (b["continente"] == continente for b in continentes):
        print(f"Países de {continente}")
        for c in continentes: 
            if c["continente"] == continente:
                print(f"País - {c["nombre"]}  Población - {c['poblacion']}  Superficie - {c['superficie']}")
    else:
        print("ERROR - El continente no esta en los archivos")

def filtrar_x_poblacion(paises): #Función que pide un rango de población y muestra todos los países dentro del rango
    minimo = validar_num("Ingresa el mínimo de población: ")
    maximo = validar_num("Ingresar el máximo de población: ")
    if minimo < maximo:
        with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
            lector = csv.DictReader(archivo) 
            poblacion = list(lector)
        if any ( minimo < int(p["poblacion"]) < maximo for p in poblacion):
            print(f"Paises entre {minimo} y {maximo} de población")
            for p in poblacion:
                if minimo < int(p["poblacion"]) < maximo:
                    print(f"País - {p["nombre"]}   Población - {p["poblacion"]}")
        else:
            print("No hay ningún país en ese rango")
    else:
        print("ERROR - El mínimo no puede ser mayor al máximo")

def filtrar_x_superficie(paises): #Función que pide un rango de superficie y muestra todos los países dentro del rango
    minimo = validar_num("Ingresa el mínimo de superficie: ")
    maximo = validar_num("Ingresar el máximo de superficie: ")
    if minimo < maximo:
        with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
            lector = csv.DictReader(archivo) 
            superficies = list(lector)
        if any ( minimo < int(s["superficie"]) < maximo for s in superficies):
            print(f"Paises entre {minimo} y {maximo} de superficie")
            for s in superficies:
                if minimo < int(s["superficie"]) < maximo:
                    print(f"País - {s["nombre"]}   Superficie - {s["superficie"]}")
        else:
            print("No hay ningún país en ese rango")
    else:
        print("ERROR - El mínimo no puede ser mayor al máximo")