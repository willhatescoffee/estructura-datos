#hacer un programa que capture los siguientes datos de alumnos
#nombre, apellido materno, apellido paterno
#fecha de naicmiento en formato dd/mm/aaaa
#guardar los datos en objetos 
#mostrar esos objetos 
#y que con escribir STOP se detenga la ejecucion 


class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}\n")


def main():
    lista_alumnos = []

    while True:
        nombre = input("Ingrese el nombre del alumno (o escriba STOP para detenerse): ")
        
        if nombre.upper() == "STOP":
            break

        apellido_paterno = input("Ingrese el apellido paterno: ")
        apellido_materno = input("Ingrese el apellido materno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato dd/mm/aaaa: ")

        alumno = Alumno(nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        lista_alumnos.append(alumno)

    print("\nDatos de los alumnos:")
    for alumno in lista_alumnos:
        alumno.mostrar_datos()

if __name__ == "__main__":
    main()



