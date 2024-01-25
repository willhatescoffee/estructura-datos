#suma de elementos de un array

def suma_array_recursiva(array, indice=0):
    if indice == len(array):
        return 0
    else:
        return array[indice] + suma_array_recursiva(array, indice + 1)

#Ejemplo de uso 
mi_array = [1, 2, 3, 4, 5]
resultado = suma_array_recursiva(mi_array)
print(resultado)
