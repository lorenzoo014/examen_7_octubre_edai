
class Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota= nota
        print("El alumno se ha creado con éxito")
    
    def calificacion(self):
        # True if self.nota>=5 else False
        if self.nota>=5:
            return True
        else:
            return False

    def __str__(self):
        return "(El nombre es: {}, y su nota es: {})".format( self.nombre, str(self.calificacion) )