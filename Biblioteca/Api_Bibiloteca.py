from Autor import Autor
from Libro import Libro
from Base_de_Datos import BaseDeDatos

class Api_Biblioteca:
    def __init__(self):
        self.db = BaseDeDatos()

        #-------autor----------

    def registrar_autor(self, nombre, nacionalidad, fecha_nacimiento, biografia):
        for autor in self.db.obtener_autores():
            if autor.nombre_completo.lower() == nombre.lower():
                return "El autor ya está registrado."
                

        nuevo_autor = Autor(nombre, nacionalidad, fecha_nacimiento, biografia)
        self.db.guardar_autor(nuevo_autor)
        return "Autor registrado exitosamente."
    
    def buscar_autor(self, nombre):
        for autor in self.db.obtener_autores():
            if autor.nombre_completo.lower() == nombre.lower():
                return autor
        return None
    
    def listar_autores_estilo_api(self):
        return [
            {
                "id": autor.id,
                "nombre": autor.nombre_completo,
                "nacionalidad": autor.nacionalidad,
                "fecha_nacimiento": autor.fecha_nacimiento,
                "biografia": autor.biografia
            }
            for autor in self.db.obtener_autores()
        ]
    
    #-------libro----------

    def registrar_libro(self, titulo, genero, fecha_publicacion, paginas, resumen, nombre_autor):
        autor=self.buscar_autor(nombre_autor)

        if not autor:
            autor = Autor(
                nombre_autor,
                "Desconocida",
                "0000-00-00",
                "Biografía no disponible."
            )
            self.db.guardar_autor(autor)

        for libro in self.db.obtener_libros():
            if libro.titulo.lower() == titulo.lower() and libro.autor.id == autor.id:
                return "El libro ya está registrado."
            
        nuevo_libro = Libro(titulo, genero, fecha_publicacion, paginas, resumen, autor)
        self.db.guardar_libro(nuevo_libro)
        return "Libro registrado exitosamente."

        


