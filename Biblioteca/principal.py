from Api_Bibiloteca import Api_Biblioteca

def main():
    biblioteca = Api_Biblioteca()

    ## Registrar un autor y un libro

    print(biblioteca.registrar_autor(
        "Gabriel García Márquez",
        "Colombiana",
        "1927-03-06",
        "Premio Nobel de Literatura"
    ))

    print(biblioteca.registrar_libro(
        "Cien años de soledad",
        "Realismo mágico",
        "1967-05-30",
        471,
        "Historia de los Buendía",
        "Gabriel García Márquez"
    ))

    ##buscar autor
    autor = biblioteca.buscar_autor("Gabriel García Márquez")
    print("\nAutor encontrado:")
    if autor:
        print(autor)
    else:
        print("Autor no encontrado")

    #listar autores (estilo API)
    print("\n📚 LISTADO DE AUTORES (ESTILO API)\n")

    autores = biblioteca.listar_autores_estilo_api()
    if not autores:
        print("No hay autores registrados.")
    else:
        print(autores)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
