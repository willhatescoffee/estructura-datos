def contar_digitos(numero):
    # Convertir el número a cadena para facilitar el conteo de dígitos
    numero_str = str(numero)
    # Usar la función len para obtener la longitud de la cadena, que es la cantidad de dígitos
    cantidad_digitos = len(numero_str)
    return cantidad_digitos

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
cantidad_digitos = contar_digitos(numero)
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
