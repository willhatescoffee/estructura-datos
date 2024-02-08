#HACER UN PROGRAMA EN PYTHON QUE HAGA  2 COSAS 

#1. DETERMINAR SI UNA PALABRA ES UN PALINDROMO  
#2. OBTENER EL TIEMPO DE EJECUCION DEL PROGRAMA

import time

def es_palindromo_recursivo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo_recursivo(palabra[1:-1])

def medir_tiempo_ejecucion(funcion, *args):
    inicio = time.time()  # Tiempo de inicio
    resultado = funcion(*args)
    fin = time.time()  # Tiempo de finalización
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion

if __name__ == "__main__":
    while True:
        print("\nMenú:")
        print("1. Programa palíndromo (recursivo)")
        print("2. Medir tiempo de ejecución del algoritmo recursivo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            palabra = input("Introduce una palabra: ")
            if es_palindromo_recursivo(palabra):
                print(f"{palabra} es un palíndromo.")
            else:
                print(f"{palabra} no es un palíndromo.")
        elif opcion == "2":
            palabra = input("Introduce una palabra para medir el tiempo de ejecución: ")
            resultado, tiempo = medir_tiempo_ejecucion(es_palindromo_recursivo, palabra)
            if resultado:
                print(f"{palabra} es un palíndromo.")
            else:
                print(f"{palabra} no es un palíndromo.")
            print(f"Tiempo de ejecución: {tiempo} segundos.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

