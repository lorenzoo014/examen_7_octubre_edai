import pytest
from Ejercicio_2.Alumno import Alumno
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/1.EDAI_2/examen_7_octubre_edai/Ejercicio_2")
#creacion de los alumnos
alumno1 = Alumno("Lorenzo",3)
alumno2 = Alumno("Raúl",5)
alumno3 = Alumno("Íñigo",7)

def test_calificacion():
    assert str(alumno1)==print(alumno1)
"""
Ejecutamos los print por pantalla
"""
print(alumno1)
 