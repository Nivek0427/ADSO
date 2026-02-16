from Autor import Autor
from Libro import Libro
from Base_de_Datos import BaseDeDatos

class Api_Biblioteca:
    def __init__(self):
        self.db = BaseDeDatos()

        #-------autor----------

    #método para registrar un nuevo autor, verificando que no exista previamente por su nombre completo
    def registrar_autor(self, nombre, nacionalidad, fecha_nacimiento, biografia):
        for autor in self.db.obtener_autores():
            if autor.nombre_completo.lower() == nombre.lower():
                return "El autor ya está registrado."
                

        nuevo_autor = Autor(nombre, nacionalidad, fecha_nacimiento, biografia)
        self.db.guardar_autor(nuevo_autor)
        return "Autor registrado exitosamente."
    
    #método para buscar un autor por su nombre completo, devolviendo el objeto Autor o None si no se encuentra
    def buscar_autor(self, nombre):
        for autor in self.db.obtener_autores():
            if autor.nombre_completo.lower() == nombre.lower():
                return autor
        return None
    
    #método para listar todos los autores en formato de diccionario, ideal para una API REST
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

    #Métodos para gestionar autores en la lista interna
    #método para insertar un autor destacado al inicio de la lista
    def insertar_autor_destacado(self, autor):
        self.autores.insert(0, autor)

    #método para eliminar un autor por su nombre completo
    def eliminar_autor_por_nombre(self, nombre):
        for autor in self.autores:
            if autor.nombre_completo == nombre:
                self.autores.remove(autor)
                return True
        return False
    
    #método para obtener la posición de un autor en la lista por su nombre completo
    def posicion_autor(self, nombre):
        nombres = [autor.nombre_completo for autor in self.autores]
        return nombres.index(nombre)
    
    #método para ordenar la lista de autores alfabéticamente por su nombre completo
    def ordenar_autores_por_nombre(self):
        self.autores.sort(key=lambda autor: autor.nombre_completo)

    #método para invertir el orden de la lista de autores
    def invertir_orden_autores(self):
        self.autores.reverse()

    
    #-------libro----------

    #método para registrar un nuevo libro, verificando que no exista previamente por su título y autor
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

    #método para eliminar el último libro registrado
    def eliminar_ultimo_libro(self):
        if self.libros:
            return self.libros.pop()
        return None
    
    #método para contar cuántos libros hay de un autor específico
    def contar_libros_autor(self, nombre_autor):
        return self.autores_libros.count(nombre_autor)

    




