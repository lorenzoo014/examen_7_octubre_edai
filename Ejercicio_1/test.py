import pytest
from Ejercicio_1.Alumno import Alumno

#creacion de los alumnos
alumno1 = Alumno("Lorenzo",3)
alumno2 = Alumno("Raúl",5)
alumno3 = Alumno("Íñigo",7)
print()

def test_calificacion():
    assert alumno1.calificacion()==False
    assert alumno2.calificacion()==True
    assert alumno3.calificacion()==True
"""
Tener en cuenta que esto se esta ejecutando desde la terminal

"""
 