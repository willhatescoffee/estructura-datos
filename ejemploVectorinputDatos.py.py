#Declaramos 2 vectores 
#Estos vectores seran homogeneos
nombres = []
identificadores = []
suma =[] 
#Definimos un tamaño para los vectores
#lo puedes cambiar si quieres, antes de la compilacion 
size = 3 

#llemos los datos y los agregamos a la lista 
for i in range(size):
    print("Ingrese los datos de la persona", i + 1)
    input_nombre = input("Nombre: ")
    identificacion = input("identificacion: ")
    
    identificadores.append(identificacion)
    nombres.append(input_nombre)

print(nombres)
print(identificadores)


suma.append (nombres)
suma.append(identificadores)
print("sumando vectores")
print(suma) #el resultado es un vector heterogeneo





