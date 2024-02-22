class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListasSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza 
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        #No sea None o Nell 
        while actual. siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    
    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end =" -> ")
            actual = actual.siguiente
        print("None")

#Ejemplo de uso
lista = ListasSimplementeEnlazada()
lista.agregar_al_final(4)
lista.imprimir_lista()
lista.agregar_al_principio(3)
lista.imprimir_lista()
lista.agregar_al_principio(2)
lista.imprimir_lista()
lista.agregar_al_final(5)
lista.imprimir_lista()
