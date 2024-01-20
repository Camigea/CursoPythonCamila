DatosAlumnos2024={"Alumno1":
                            {"Nombre":"Camila","Apellido":"Gea","Edad": 31,"DNI":36912448,"Calificaciones":(6,7,8,9,5,6,6,7,10), "Fecha de nacimiento":"11/11/92", "Tutor": "Goldy Ulivarri", "Faltas":1, "Amonestaciones":0},
                  "Alumno2":
                            {"Nombre":"Natalia","Apellido":"Gonzalez","Edad": 31,"DNI":36912545,"Calificaciones":(6,7,8,9,5,6,6,7,4),"Fecha de nacimiento":"11/08/92", "Tutor": "Goldy Ulivarri", "Faltas":3, "Amonestaciones":1},
                  "Alumno3":
                            {"Nombre":"Camilo","Apellido":"Tonda","Edad": 30,"DNI":37912448,"Calificaciones":(6,7,8,9,10,6,6,9,9),"Fecha de nacimiento":"19/11/93", "Tutor": "Goldy Ulivarri", "Faltas":2, "Amonestaciones":2},
                  "Alumno4":
                            {"Nombre":"Daniel","Apellido":"Fernandez","Edad": 30,"DNI":37111222,"Calificaciones":(6,10,8,9,10,6,6,7,9),"Fecha de nacimiento":"11/01/93", "Tutor": "Goldy Ulivarri", "Faltas":1, "Amonestaciones":1},
                  "Alumno5":
                            {"Nombre":"Marcia","Apellido":"Lopez","Edad": 41,"DNI":26912448,"Calificaciones":(6,7,8,3,5,6,6,7,2),"Fecha de nacimiento":"20/11/82", "Tutor": "Goldy Ulivarri", "Faltas":3, "Amonestaciones":3},
                  "Alumno6":
                            {"Nombre":"Juan","Apellido":"Perez","Edad": 44,"DNI":23912545,"Calificaciones":(6,7,6,6,5,6,6,6,6),"Fecha de nacimiento":"11/5/78", "Tutor": "Goldy Ulivarri", "Faltas":2, "Amonestaciones":1},
                  "Alumno7":
                            {"Nombre":"Paula","Apellido":"Etcheverry","Edad": 34,"DNI":33912448,"Calificaciones":(6,7,8,9,9,9,9,7,10),"Fecha de nacimiento":"05/11/89", "Tutor": "Goldy Ulivarri", "Faltas":1, "Amonestaciones":4},
                  "Alumno8":
                            {"Nombre":"Ana","Apellido":"Barraguirre","Edad": 22,"DNI":46912545,"Calificaciones":(6,7,8,9,5,10,10,10,10),"Fecha de nacimiento":"11/11/01", "Tutor": "Goldy Ulivarri", "Faltas":3, "Amonestaciones":1},
                  "Alumno9":
                            {"Nombre":"Lazaro","Apellido":"Cipriani","Edad": 42,"DNI":25912448,"Calificaciones":(6,7,8,6,5,6,6,7,6),"Fecha de nacimiento":"11/9/81", "Tutor": "Goldy Ulivarri", "Faltas":2, "Amonestaciones":3},
                  "Alumno10":
                            {"Nombre":"Luciano","Apellido":"Monaco","Edad": 29,"DNI":38912545,"Calificaciones":(6,7,8,9,10,10,10,7,4),"Fecha de nacimiento":"11/11/95", "Tutor": "Goldy Ulivarri", "Faltas":1, "Amonestaciones":1},
                  "Alumno11":
                            {"Nombre":"Harley","Apellido":"Quinn","Edad": 34,"DNI":33912448,"Calificaciones":(9,9,9,9,5,6,6,7,10),"Fecha de nacimiento":"11/11/89", "Tutor": "Goldy Ulivarri", "Faltas":3, "Amonestaciones":2},
                  "Alumno12":
                            {"Nombre":"Equilberto","Apellido":"Tolaba","Edad": 23,"DNI":47912545,"Calificaciones":(10,10,10,10,10,10,10,10,10),"Fecha de nacimiento":"11/11/00", "Tutor": "Goldy Ulivarri", "Faltas":2, "Amonestaciones":1},
                 }



def MostrarDatos (alumno):
    if alumno in DatosAlumnos2024:
        print("Datos de {}:".format(alumno))
        for key, value in DatosAlumnos2024[alumno].items():
            print("{}: {}".format(key, value))
        print()
    else:
        print("No se encontraron datos para el alumno {}.\n".format(alumno))

def ModificarDatos(alumno, nuevos_datos):
    if alumno in DatosAlumnos2024:
        for clave, valor in nuevos_datos.items():
            DatosAlumnos2024[alumno][clave] = valor
        print("Datos de {} modificados correctamente.\n".format(alumno))
    else:
        print("No se encontraron datos para el alumno {}.\n".format(alumno))

def AgregarDatos(alumno, datos_nuevos):
    if alumno not in DatosAlumnos2024:
        DatosAlumnos2024[alumno] = datos_nuevos
        print("Alumno {} agregado correctamente.\n".format(alumno))
    else:
        print("El alumno {} ya existe en la base de datos.\n".format(alumno))

def ExpulsarAlumno(alumno):
    if alumno in DatosAlumnos2024:
        del DatosAlumnos2024[alumno]
        print("Alumno {} expulsado correctamente.\n".format(alumno))
    else:
        print("No se encontraron datos para el alumno {}.\n".format(alumno))

MostrarDatos("Alumno1")
ModificarDatos("Alumno2", {"Faltas": 0})
AgregarDatos("Alumno13", {"Nombre": "Nuevo", "Apellido": "Alumno", "Edad": 25, "DNI": 12345678,
                            "Calificaciones": (8, 9, 7, 6, 8, 9, 10, 8, 7), "Fecha de nacimiento": "01/01/99",
                            "Tutor": "Nuevo Tutor", "Faltas": 2, "Amonestaciones": 1})
ExpulsarAlumno("Alumno3")

    