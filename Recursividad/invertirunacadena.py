def invertir_cadena(cadena):
    # Utilizar el slicing con paso -1 para invertir la cadena
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Ejemplo de uso
cadena_original = input("Ingrese una cadena: ")
cadena_resultado = invertir_cadena(cadena_original)
print(f"La cadena invertida de '{cadena_original}' es '{cadena_resultado}'")
