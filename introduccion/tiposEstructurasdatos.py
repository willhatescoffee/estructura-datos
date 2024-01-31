
#Estructura lineal homogenea
#estructuraLineal = [2,4,5,7]
#print (estructuraLineal)
#print ("el array tiene un tamaño", len(estructuraLineal))

##estructuras lineales heterogeneas 
#estructuraHeterogenea = [1,'1','hola',True,5.2]
#print(estructuraHeterogenea[2])
#print ("el array heterogeneo tiene un tamaño", len(estructuraHeterogenea))

cola = []
size = 3

for i in range(size):
    input_num = int(input("Numero: "))
    cola.append(input_num)

print(cola)
print(cola.pop())
