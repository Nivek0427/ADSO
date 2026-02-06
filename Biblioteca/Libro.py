import uuid

class Libro:
    def __init__(self, titulo, genero, fecha_publicacion, paginas, resumen, autor):
        self.codigo = str(uuid.uuid4())
        self.titulo = titulo
        self.genero = genero
        self.fecha_publicacion = fecha_publicacion
        self.paginas = paginas
        self.resumen = resumen
        self.autor = autor

    def __str__(self):
        return (
            f"Código: {self.codigo}\n"
            f"Título: {self.titulo}\n"
            f"Género: {self.genero}\n"
            f"Fecha de publicación: {self.fecha_publicacion}\n"
            f"Páginas: {self.paginas}\n"
            f"Autor: {self.autor.nombre_completo}\n"
            f"Resumen: {self.resumen}"
        )
    
    def get_titulo(self):
        return self.titulo
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_genero(self):
        return self.genero
    def set_genero(self, nuevo_genero):
        self.genero = nuevo_genero

    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    def set_fecha_publicacion(self, nueva_fecha_publicacion):
        self.fecha_publicacion = nueva_fecha_publicacion

    def get_paginas(self):
        return self.paginas
    def set_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas

    def get_resumen(self):
        return self.resumen
    def set_resumen(self, nuevo_resumen):
        self.resumen = nuevo_resumen

    def get_autor(self):
        return self.autor
    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    
