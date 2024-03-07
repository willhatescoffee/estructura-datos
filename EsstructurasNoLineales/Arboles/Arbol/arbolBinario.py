class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:

    def preorden(NodoArbol):
        if NodoArbol is not None:
            print(NodoArbol.valor)
            preorden(nodo.izquierda)
            preorden(nodo.derecha)



#crear nodos
nodo1 = NodoArbol (1)
nodo2 = NodoArbol (2)
nodo3 = NodoArbol (3)

#conectar nodos
nodo1.izquierda = nodo2
nodo1.derecha = nodo3