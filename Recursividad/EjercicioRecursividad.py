#hacer una funcion recursiva para sumar numeros naturales 

def suma_naturales_entre_limites(inicio, fin):
    if inicio > fin:
        return 0
    else:
        return inicio + suma_naturales_entre_limites(inicio + 1, fin)

inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

if inicio < 0 or fin < 0 or inicio > fin:
    print("Por favor, ingrese dos números naturales válidos (el segundo mayor o igual al primero).")
else: 
    resultado = suma_naturales_entre_limites(inicio, fin)
    print(f"La suma de los números naturales entre {inicio} y {fin} es: {resultado}")




#Hacer una funcion recursiva para sumar numeros naturales

def suma_dos_numeros_recursiva(a, b):
# Caso Base
    if b == 0:
        return a
# Llamada Recursiva
    else:
        print (a+1, b-1)

        return suma_dos_numeros_recursiva(a + 1, b - 1)

# Ejemplo de uso
num1 = 3
num2 = 4
resultado = suma_dos_numeros_recursiva(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")