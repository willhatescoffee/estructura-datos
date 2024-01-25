def torres_hanoi(n,origen,destino,auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        #Caso recursivo
        #paso 1: Mueve la torre mas peqieña de origen a auxiliar
        torres_hanoi(n-1,origen,auxiliar,destino)

        #paso 2: mueve el disco mas grande de origen a destino
        print(f"mover disco {n} de {origen} a {destino}")

        #paso 3: mueve la torre de auxiliar a destino, utilzando origen como auxiliar 
        torres_hanoi(n-1,auxiliar,destino,origen)

#ejemplo de uso con 3 discos de "A" a "C", usando "B" como auxiliar 
        torres_hanoi(3, "A", "B", "C")
        