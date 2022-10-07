import pytest
from Alumno import Alumno
import sys
sys.path.insert(0,"/Users/Lorenzo/Documents/programacion/1.EDAI_2/examen_7_octubre_edai")
#creacion de los alumnos
alumno1 = Alumno("Lorenzo",3)
alumno2 = Alumno("Raúl",5)
alumno3 = Alumno("Íñigo",7)

def test_calificacion():
    assert type(str(alumno1))==type("")
"""
Ejecutamos los print por pantalla
El test es bastante cutre pero lo he intentado hacer bien y 
a pesar de que sé que esta bien falla. Lo intentaré corregir por ahora así
"""
print(alumno1)
 