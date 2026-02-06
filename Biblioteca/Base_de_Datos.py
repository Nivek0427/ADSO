class BaseDeDatos:
    def __init__(self):
        self.autores = []
        self.libros = []

    # AUTORES
    def guardar_autor(self, autor):
        self.autores.append(autor)

    def obtener_autores(self):
        return self.autores

    # LIBROS
    def guardar_libro(self, libro):
        self.libros.append(libro)

    def obtener_libros(self):
        return self.libros
