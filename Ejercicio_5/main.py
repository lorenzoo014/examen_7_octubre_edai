#lanzador
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/1.EDAI_2/examen_7_octubre_edai")
from Vehiculo import Vehiculo,Camioneta,Bicicleta,Motocicleta,Coche,catalogar,catalogar




camioneta1 = Camioneta("rojo",4,130,1100,500)
bicicleta1 = Bicicleta("verde",2,"urbana")
Motocicleta1 = Motocicleta("naranja",2,"deportiva",120,1000)
c = Coche("azul", 4, 150, 1200)

lista_vehiculos =[]
lista_vehiculos.append(c)
lista_vehiculos.append(camioneta1)
lista_vehiculos.append(bicicleta1)
lista_vehiculos.append(Motocicleta1)


def pruebas():
    while True:
        print("========================")
        print(" BIENVENIDO AL Manager ")
        print("========================")
        print("[1]  Funciones_catalogar ")
        print("[2] Cerrar el Manager ")
        print("========================")
        opcion = input("> ")
        #--------1era_opcion--------#
        if opcion == "1":
            print("\nComprobamos la funcion catalogar: ")
            catalogar(lista_vehiculos)
            print("\n Comprobamos la funcion catalogar con el polimorfismo de sobreecarga correspondiente : ")
            catalogar(lista_vehiculos, 2)
            catalogar(lista_vehiculos, 4)
            catalogar(lista_vehiculos, 0)

        if opcion == '2':
            print("Saliendo...\n")
            break
input("\nPresiona ENTER para continuar...")
# pruebas() -->se podría ejecutar el main directamente poniendo esta sentencia

