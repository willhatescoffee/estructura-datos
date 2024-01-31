#hacer un programa que genere una curp hipotetica tomando los siguientes valores
#inicial del apellido Paterno y Materno, como la inicial del nombre(s)

def generar_curp (apellido_paterno, apellido_materno, nombres):
    inicial_paterno = apellido_paterno[0].upper()
    inicial_materno = apellido_materno[0].upper()
    iniciales_nombres = "".join([nombre[0].upper() for nombre in nombres.split()])
    
    año_nacimiento = "05"
    mes_dia_nacimiento = "1206"
    sexo = "M"
    estado = "MEX"
    digito_verificador = "1"
    
    curp = inicial_paterno + inicial_materno + iniciales_nombres + año_nacimiento + mes_dia_nacimiento + sexo + estado + digito_verificador

    return curp

apellido_paterno = input("Ingrese el apellido paterno: ")
apellido_materno = input("Ingrese el apeliido materno: ")
nombres = input("Ingrese el/los nombre(s): ")

curp_generada = generar_curp(apellido_paterno, apellido_materno, nombres)
print("La CURP generada es: ", curp_generada)




  