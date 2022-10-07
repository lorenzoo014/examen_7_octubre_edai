class Producto():
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("El Producto ha sido creado con exito")

    def __str__(self):
        return "(Producto:\n El codigo es: {}, su nombre es: {},su precio es: {},su tipo es: {})".format( self.codigo
        , self.nombre,self.precio,self.tipo )
        