def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado

# Ejemplo de uso
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")
