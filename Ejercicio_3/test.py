"""
docstring:
TENER EN CUENTA:
aunque este archivo se llama test.py no va a realizar test solo se va a ejecutar el main

intentaré modificar el pytest mas adelante
"""
import pytest
from Producto import Producto
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/1.EDAI_2/examen_7_octubre_edai")
#creacion de los productos
#codigo,nombre,precio,tipo
producto1 = Producto(20,"Lorenzo",30,"A")
producto2 = Producto(10,"Raúl",35,"C")
producto3 = Producto(4,"Íñigo",40,"B")
print(producto1)
print(producto2)
print(producto3)
# def modificar_valores():

