class Alumno:
    def __init__(self, nombre, apellido, edad, dni, calificaciones, fecha_nacimiento, tutor, faltas, amonestaciones):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.calificaciones = calificaciones
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.faltas = faltas
        self.amonestaciones = amonestaciones

    def mostrar_datos(self):
        print("Datos de {}:".format(self.nombre))
        print("Nombre: {}".format(self.nombre))
        print("Apellido: {}".format(self.apellido))
        print("Edad: {}".format(self.edad))
        print("DNI: {}".format(self.dni))
        print("Calificaciones: {}".format(self.calificaciones))
        print("Fecha de nacimiento: {}".format(self.fecha_nacimiento))
        print("Tutor: {}".format(self.tutor))
        print("Faltas: {}".format(self.faltas))
        print("Amonestaciones: {}".format(self.amonestaciones))
        print()

    def agregar_nota(self, nota):
        self.calificaciones += (nota,)

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1


DatosAlumnos2024 = {"Alumno1": Alumno("Camila", "Gea", 31, 36912448, (6, 7, 8, 9, 5, 6, 6, 7, 10), "11/11/92", "Goldy Ulivarri", 1, 0),
                    "Alumno2": Alumno("Natalia", "Gonzalez", 31, 36912545, (6, 7, 8, 9, 5, 6, 6, 7, 4), "11/08/92", "Goldy Ulivarri", 3, 1),
                    "Alumno3": Alumno("Camilo", "Tonda", 30, 37912448, (6, 7, 8, 9, 10, 6, 6, 9, 9), "19/11/93", "Goldy Ulivarri", 2, 2),"Alumno4": Alumno("Daniel", "Fernandez", 30, 37111222, (6, 10, 8, 9, 10, 6, 6, 7, 9), "11/01/93", "Goldy Ulivarri", 1, 1),
                    "Alumno5": Alumno("Marcia", "Lopez", 41, 26912448, (6, 7, 8, 3, 5, 6, 6, 7, 2), "20/11/82", "Goldy Ulivarri", 3, 3),
                    "Alumno6": Alumno("Juan", "Perez", 44, 23912545, (6, 7, 6, 6, 5, 6, 6, 6, 6), "11/5/78", "Goldy Ulivarri", 2, 1),
                    "Alumno7": Alumno("Paula", "Etcheverry", 34, 33912448, (6, 7, 8, 9, 9, 9, 9, 7, 10), "05/11/89", "Goldy Ulivarri", 1, 4),
                    "Alumno8": Alumno("Ana", "Barraguirre", 22, 46912545, (6, 7, 8, 9, 5, 10, 10, 10, 10), "11/11/01", "Goldy Ulivarri", 3, 1),
                    "Alumno9": Alumno("Lazaro", "Cipriani", 42, 25912448, (6, 7, 8, 6, 5, 6, 6, 7, 6), "11/9/81", "Goldy Ulivarri", 2, 3),
                    "Alumno10": Alumno("Luciano", "Monaco", 29, 38912545, (6, 7, 8, 9, 10, 10, 10, 7, 4), "11/11/95", "Goldy Ulivarri", 1, 1),
                    "Alumno11": Alumno("Harley", "Quinn", 34, 33912448, (9, 9, 9, 9, 5, 6, 6, 7, 10), "11/11/89", "Goldy Ulivarri", 3, 2),
                    "Alumno12": Alumno("Equilberto", "Tolaba", 23, 47912545, (10, 10, 10, 10, 10, 10, 10, 10, 10), "11/11/00", "Goldy Ulivarri", 2, 1),
                }


def mostrar_datos(alumno):
    if alumno in DatosAlumnos2024:
        DatosAlumnos2024[alumno].mostrar_datos()
    else:
        print(f"No se encontraron datos para el alumno {alumno}.\n")


def modificar_datos(alumno, nuevos_datos):
    if alumno in DatosAlumnos2024:
        for clave, valor in nuevos_datos.items():
            setattr(DatosAlumnos2024[alumno], clave, valor)
        print("Datos de {} modificados correctamente.\n".format(alumno))
    else:
        print("No se encontraron datos para el alumno {}.\n".format(alumno))


def agregar_datos(alumno, datos_nuevos):
    if alumno not in DatosAlumnos2024:
        DatosAlumnos2024[alumno] = Alumno(**datos_nuevos)
        print("Alumno {} agregado correctamente.\n".format(alumno))
    else:
        print("El alumno {} ya existe en la base de datos.\n".format(alumno))


def expulsar_alumno(alumno):
    if alumno in DatosAlumnos2024:
        del DatosAlumnos2024[alumno]
        print("Alumno {} expulsado correctamente.\n".format(alumno))
    else:
        print("No se encontraron datos para el alumno {}.\n".format(alumno))



mostrar_datos("Alumno10")
modificar_datos("Alumno2", {"faltas": 0})
agregar_datos("Alumno13", {"nombre": "Nuevo", "apellido": "Alumno", "edad": 25, "dni": 12345678,
                            "calificaciones": (8, 9, 7, 6, 8, 9, 10, 8, 7), "fecha_nacimiento": "01/01/99",
                            "tutor": "Nuevo Tutor", "faltas": 2, "amonestaciones": 1})
expulsar_alumno("Alumno3")
