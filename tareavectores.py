#crear un programa que almacene nombres en un vector 
#capturara datos hasta que el valor ingresado sea "STOP"
#mostrar el vector resultante
#sugerencia : usar metodo while


nombres = []

while True:
    nombre = input("Ingrese un nombre (o escriba 'STOP' para finalizar): ")
        
    if nombre.upper () == "STOP":
        break
      
    nombres.append(nombre)

print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)
