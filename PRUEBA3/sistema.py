import funciones as fun
import os

while True:
    fun.limpiar()
    print("""----------------------
Colegio San Charlis
----------------------
1)Registrar alumno
2)Buscar alumno
3)Imprimir certificados
0)Salir""")
    op=int(input("\nSeleccione : "))
    os.system('cls')

    if op==0:
        print("Adios :)")
        break
    elif op==1:
        print("Registrar alumno\n")
        rut = input("Ingrese rut : ")
        nombre = input("Ingrese nombre : ").capitalize()
        edad = int(input("Ingrese edad : "))
        genero = input("Ingrese genero (M/F): ").capitalize()
        promedio = int(input("Ingrese promedio (ej:53) : "))
        matricula = input("Ingrese fecha matricula : ")
        apoderado = input("Ingrese nombre del apoderado : ").capitalize()
        fun.registraralumno(rut,nombre,edad,genero,promedio,matricula,apoderado)

    elif op==2:
        print("Buscar alumno\n")
        rut = input("Ingrese rut : ")
        os.system('cls')
        fun.buscaralumno(rut)

    elif op==3:
        print("""---------------------
Imprimir certificados
---------------------
1)Anotaciones del alumno
2)Certificado de notas
3)Certificado alumno regular""")
        cert=int(input("\nSeleccione : "))
        if cert==1:
            print("Anotaciones del alumno")
            rut = input("Ingrese rut : ")
            os.system('cls')
            fun.anotaciones(rut)
        elif cert==2:
            print("Certificado de notas")
            rut = input("Ingrese rut : ")
            os.system('cls')
            fun.Cnotas(rut)
        elif cert==3:
            print("Certificado alumno regular")
            rut = input("Ingrese rut : ")
            os.system('cls')
            fun.alumnoregular(rut)
        else:
            print("\nSeleccion no valida")
    else:
        print("Opcion no valida")