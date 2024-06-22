import os 

libros = []
usuarios = []
LibroSKU = []
prestamos = []
def registrar_libro():
    try:
        titulo = input("Ingrese el titulo del libro que desea registrar: ")
        Autor = input("Ingrese el autor del libro: ")
        Año_De_Publicacion = int(input("Ingrese el año de publicación del libro: "))
        SKU = input("ingrese el SKU del libro, tenga en cuenta que el SKU es las 6 primeras letras del título del libro, las 3 primeras letras del autor y el año de publicación, separados por guion(XXXXXX-XXX-XXXX): ")
        LibroSKU.append(SKU)
        if titulo == "" or Autor == "" or Año_De_Publicacion <= 0 or SKU == "":
            raise ValueError("Error en los datos ingresados, uno o mas son erroneos, intente nuevamente. ")
        
        libro = {
            "Titulo": titulo,
            "Autor": Autor,
            "Año de publicacion": Año_De_Publicacion,
            "SKU": SKU
        }

        libros.append(libro)
        print("Se registro el libro exitosamente. ")
    except ValueError as m:
        print(m)

def lista_libros(): 
    if not libros:
        print("No hay libros registrados")
    else:
        for libro in libros:
            print(f"Titulo: {libro["Titulo"]} \t Autor: {libro['Autor']} \t Año de publicacion: {libro['Año de publicacion']} \t SKU: {libro['SKU']}")

def prestamo_libro():
    try: 
        usuario = input("ingrese el nombre del usuario: ")
        usuarios.append(usuario)
        print("Usuario registrado.")
        Titulo = input("Ingrese el titulo del libro: ")
        PrestamoSKU = input("Ingrese el SKU del libro: ")
        prestamos.append(PrestamoSKU)
        if PrestamoSKU == "":
            print("SKU invalido, intente nuevamente. ")
        elif PrestamoSKU == prestamos:
            print("Este libro ya fue prestado. ")
        fecha_prestamo = input("ingrese la fecha del prestamo. ")

        LibroP = {
            "usuario": usuario,
            "Titulo": Titulo,
            "PrestamoSKU": PrestamoSKU,
            "Fecha prestamo": fecha_prestamo
        }
        prestamos.append(LibroP)
    except ValueError as m:
        print(m)

def reporte_prestamos():
    try: 
        op = int(input("¿Desea imprimir el reporte de prestamos? \t1.si \t2.no: "))
        if op == 1:
            filename = "Reporte_Prestamos"
        elif op == 2:
            print("")
        else:
            raise ValueError("Opcion no valida, intente nuevamente")      
        
        with open(filename, "w") as archivo:
            for LibroP in prestamos:
                if op == 1:
                    archivo.write(f"Usuario: {LibroP['usuario']} \t Titulo: {libros["Titulo"]} \t Fecha de prestamo: {LibroP["Fecha prestamo"]}")
        print(f"El reporte se genero exitosamente en: {os.getcwd()}")

    except ValueError as m:
        print(m)
def app():
    while True:
        try: 
            print("----APP----")
            print("1. Registrar libro \n2. Prestar libro \n3. Listar todos los libros \n4. Imprimir reporte de prestamos \n5. Salir del programa")
            op = int(input("Ingrese una opcion:\t"))
            if op == 1:
                registrar_libro()
            elif op == 2:
                prestamo_libro()
            elif op == 3:
                lista_libros()
            elif op == 4: 
                reporte_prestamos()
            elif op == 5: 
                print("Programa finalizado…\nDesarrollado por Mauro Opazo \nRUN: 21.879.856-K")
                break
            else: 
                print("Opcion invalida, intente nuevamente")
        except ValueError as m:
            print(m)