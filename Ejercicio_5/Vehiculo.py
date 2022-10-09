class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )

#----------Herencia de los vehículos de 4 ruedas-------#
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):
    def __init__(self,color, ruedas, velocidad, cilindrada,carga):
        Coche.__init__(self, color, ruedas,velocidad,cilindrada)
        self.carga=carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kilos".format(self.carga)



#----------herencia de los vehiculos de 2 ruedas----------#
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} ".format(self.tipo)



class Motocicleta(Bicicleta):
    def __init__(self,color, ruedas, tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}".format(self.velocidad, self.cilindrada)






#----------funcion_catalogar----------#

# def catalogar(lista):
#     for vehiculo in lista:
#         informacion = "El vehiculo es un "+ type(vehiculo).__name__+" y sus atributos son: "+ str(vehiculo)
#         print(informacion)

#----------funcion_catalogar_polimorfismo_de_sobrecarga----------#
def catalogar(lista, ruedas):
    contador =0
    print("\n")
    for vehiculo in lista:
        informacion = "El vehiculo es un/a "+ type(vehiculo).__name__+" y sus atributos son: "+ str(vehiculo)
        if (vehiculo.ruedas == ruedas):
            contador +=1
            print(informacion)
    # print(contador)
    if(contador ==0):
        print("No hay ningun vehiculo con {} ruedas".format(str(ruedas)))
    print("Por lo tanto, se han encontrado {} vehiculos con {} ruedas".format(str(contador),str(ruedas)))