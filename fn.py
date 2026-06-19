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

def cargar_pais(paises): #Funcion que recibe los datos del usuario y carga un nuevo país
    nombre = validar_str("Ingresa el nombre del país: ")
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        datos = list(lector)
        encabezados = lector.fieldnames
    if any(p['nombre'] == nombre for p in datos):
        print("País ya cargado en el archivo\n")
    else:
        nuevo_pais = {}
        nuevo_pais['nombre'] = nombre
        nuevo_pais['poblacion'] = validar_num(f"Ingresa la población de {nombre}: ")
        nuevo_pais['superficie'] = validar_num(f"Ingresa la superficie de {nombre}: ")
        nuevo_pais['continente'] = validar_str(f"Ingresa a que continente pertenece {nombre}: ")
        with open(paises, "a", encoding = "utf-8", newline = "") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor.writerow(nuevo_pais)
        print(f"País cargado - {nombre}  Población - {nuevo_pais['poblacion']}  Superficie - {nuevo_pais['superficie']}  Continente - {nuevo_pais['continente']} ")

def actualizar_pais(paises): #Función que recibe un país ingresado por el usuario, busca en el csv si existe y luego el usuario ingresa un nuevo valor de población y superficie
    buscado = validar_str("Qué país querés modificar?: ")
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        datos = list(lector)
        encabezados = lector.fieldnames
    for p in datos:
        if p['nombre'] == buscado:
            p['poblacion'] = validar_num("Ingresá la población actualiada: ")
            p['superficie'] = validar_num("Ingresa la superficie actualizada:")
    
    with open(paises, "r+", encoding = "utf-8", newline = "") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)
    for p in datos:
        if p["nombre"] == buscado:
            print(f"País actualizado - {buscado}  Población - {p['poblacion']}  Superficie - {p['superficie']}  Continente - {p['continente']}")


def  buscar_pais(paises): #Función que recibe un nombre parcial o total y busca en el csv 
    buscado = validar_str("Qué país querés buscar?: ")
    encontrado = False
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        datos = list(lector)
    for p in datos:
        if buscado in p['nombre']:
            print(f"País - {p['nombre']}  Población - {p['poblacion']}  Superficie - {p['superficie']}  Continente - {p['continente']}")
            encontrado = True
    if not encontrado:
        print(f"{buscado} no coincide parcial ni totalmente con ningún país del archivo")

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
    if any (b['continente'] == continente for b in continentes):
        print(f"Países de {continente}")
        for c in continentes: 
            if c['continente'] == continente:
                print(f"País - {c['nombre']}  Población - {c['poblacion']}  Superficie - {c['superficie']}")
    else:
        print("ERROR - El continente no esta en los archivos")

def filtrar_x_poblacion(paises): #Función que pide un rango de población y muestra todos los países dentro del rango
    minimo = validar_num("Ingresa el mínimo de población: ")
    maximo = validar_num("Ingresar el máximo de población: ")
    if minimo < maximo:
        with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
            lector = csv.DictReader(archivo) 
            poblacion = list(lector)
        if any ( minimo < int(p['poblacion']) < maximo for p in poblacion):
            print(f"Paises entre {minimo} y {maximo} de población")
            for p in poblacion:
                if minimo < int(p['poblacion']) < maximo:
                    print(f"País - {p['nombre']}   Población - {p['poblacion']}")
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
        if any ( minimo < int(s['superficie']) < maximo for s in superficies):
            print(f"Paises entre {minimo} y {maximo} de superficie")
            for s in superficies:
                if minimo < int(s['superficie']) < maximo:
                    print(f"País - {s['nombre']}   Superficie - {s['superficie']}")
        else:
            print("No hay ningún país en ese rango")
    else:
        print("ERROR - El mínimo no puede ser mayor al máximo")

def ordenar_paises(paises): #Función que agrupa 3 tipos de orden distintos según el que quiera el usuario
    print("Tipos de orden: Nombre, Población, Superficie ascendente (SA), Superficie descendente (SD)")
    opcion = validar_str("Qué orden querés aplicar (Ingresa N, P, SA o SD)?: \n")
    match opcion:
        case "N":
            ordenar_x_nombre(paises)
        case "P":
            ordenar_x_poblacion(paises)
        case "SA" | "Sa":
            ordenar_x_sa(paises)
        case "SD" | "Sd":
            ordenar_x_sd(paises)
        case _:
            print("ERROR - Ingresa un orden válido") 

def ordenar_x_nombre(paises): #Función que ordena los países cargados en base a su nombre 
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        nombres = list(lector)
    orden_nombre = sorted(nombres, key=lambda n: n['nombre'])
    print("Lista de paises ordenados por nombre\n")
    for p in orden_nombre:
        print(f"País - {p['nombre']}  Población - {p['poblacion']}  Superficie - {p['superficie']}  Continente - {p['continente']}")

def ordenar_x_poblacion(paises): #Función que ordena los países cargados en base a su población 
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        poblaciones = list(lector)
    orden_poblacion = sorted(poblaciones, key=lambda p: int(p["poblacion"]))
    print("Lista de paises ordenados por poblacion\n")
    for p in orden_poblacion:
        print(f"País - {p['nombre']}  Población - {p['poblacion']}  Superficie - {p['superficie']}  Continente - {p['continente']}")

def ordenar_x_sa(paises): #Función que ordena los países cargados en base a su superficie de manera ascendente 
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        sa = list(lector)
    orden_sa = sorted(sa, key=lambda s: int(s['superficie']))
    print("Lista de paises ordenados por superficie ascendente\n")
    for s in orden_sa:
        print(f"País - {s['nombre']}  Población - {s['poblacion']}  Superficie - {s['superficie']}  Continente - {s['continente']}")

def ordenar_x_sd(paises): #Función que ordena los países cargados en base a su superficie de manera descendente
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        sd = list(lector)
    orden_sd = sorted(sd, key=lambda s: int(s['superficie']), reverse= True)
    print("Lista de paises ordenados por superficie descendente\n")
    for s in orden_sd:
        print(f"País - {s['nombre']}  Población - {s['poblacion']}  Superficie - {s['superficie']}  Continente - {s['continente']}")