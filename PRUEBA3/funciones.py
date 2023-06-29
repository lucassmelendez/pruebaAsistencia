import numpy as np
import os
import msvcrt
import random

total=20
alumnos = np.empty([total,7],object)

def limpiar():
    print("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system('cls')

def validaralumno(rut):
    for i in range(total):
        if alumnos[i,0]==rut:
            return i
    return -1

def registraralumno(rut,nombre,edad,genero,promedio,matriucula,apoderado):
    if None in alumnos:
        if validaralumno(rut)<0:
            if len(nombre)>=2 and len(nombre)<=30:
                if edad>=4:
                    for i in range(total):
                        if alumnos[i,0]==None:
                            alumnos[i,0]=rut
                            alumnos[i,1]=nombre
                            alumnos[i,2]=edad
                            alumnos[i,3]=genero
                            alumnos[i,4]=promedio
                            alumnos[i,5]=matriucula
                            alumnos[i,6]=apoderado
                            print(f"\nAlumno {nombre} registrado")
                            break
                else:
                    print("\nLa edad debe ser mayor o igual a 4")
            else:
                print("\nEl nombre debe tener entre 2 y 30 caracteres")
        else:
            print("\nRut repetido")
    else:
        print("\nNo hay espacio disponible")

def buscaralumno(rut):
    indice=validaralumno(rut)
    if indice>=0:
        print(f"""Alumno Encontrado :\n 
rut              : {alumnos[indice,0]} 
nombre           : {alumnos[indice,1]} 
edad             : {alumnos[indice,2]} 
genero           : {alumnos[indice,3]} 
promedio         : {alumnos[indice,4]} 
fecha matricula  : {alumnos[indice,5]} 
nombre apoderado : {alumnos[indice,6]}""")
    
    else:
        print("\nRut no registrado")

listaanotaciones=[]
listaanotaciones.append("Alumno conversa en clase")
listaanotaciones.append("Alumno interrumpe la clase")
listaanotaciones.append("Alumno rompe materia de clase")
listaanotaciones.append("Alumno se va a la mitad de la clase")
listaanotaciones.append("Alumno va al baño y no vuelve")
listaanotaciones.append("Alumno falta el respeto al inspector")
listaanotaciones.append("Alumno deja sala llena de papeles")

def anotaciones(rut):
    indice=validaralumno(rut)
    if indice>=0:
        print(f"""-----------------------------------------
Alumno : {alumnos[indice,1]}
-----------------------------------------
anotacion 1 : {listaanotaciones[random.randint(0,6)]}
anotacion 2 : {listaanotaciones[random.randint(0,6)]}
anotacion 3 : {listaanotaciones[random.randint(0,6)]}
-----------------------------------------""")
    else:
        print("\nRut no registado")

def Cnotas(rut):
    indice=validaralumno(rut)
    if indice>=0:
        print(f"""-----------------------------------------
Alumno : {alumnos[indice,1]}
-----------------------------------------
nota 1 : {random.randint(10,70)}
nota 2 : {random.randint(10,70)}
nota 3 : {random.randint(10,70)}
-----------------------------------------""")
    else:
        print("\nRut no registrado")

def alumnoregular(rut):
    indice=validaralumno(rut)
    if indice>=0:
        print(f"""------------------------------------
El alumno {alumnos[indice,1]} , RUT {alumnos[indice,0]} 
Se encuentra matriculado en el 
Colegio San Charlis de Puente Alto
------------------------------------""")
    else:
        print("\nRut no registrado")