class Errores():
    @staticmethod
    def division_cero():
        try:
            numero = 7/0
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
    @staticmethod
    def lista_indice():
        try:
            lista = [4, 7, 30, 23, 5]
            lista[10]    
        except IndexError:
            print("Se esta intentando sacar un elemento superior o inferior al tamaño de la lista")
    @staticmethod
    def diccionario_error():
        try:
            paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
            paises["alemania"]
        except KeyError:
            print("el país introducido no se encuentra en la lista")
    @staticmethod
    def suma_error():
        try:
            resultado = "2" + 10
        except TypeError:
            resultado= int("2") + 10
            print("can only concatenate str (not int) to str")

Errores.division_cero()
Errores.lista_indice()
Errores.diccionario_error()
Errores.suma_error()

