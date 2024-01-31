#Ejemplo de uso de memoria dinamica usando clases

#definicion de la clase
class ListaDinamica:
    def __init__(self):
        self.elementos = []

    def agregarElementos(self,elemento):
        self.elementos.append(elemento)

    def mostrarElementos(self):
        print("Elementos de la lista", self.elementos)

#Metodo para clase anterior
def usoMemoriaDinamica():
    new_lista: ListaDinamica() #objeto tipo lista dinamica

    new_lista.agregarElementos(10)
    new_lista.agregarElementos(20)
    new_lista.agregarElementos(30)

    new_lista.agregarElementos()

if __name__ == " __main__ ":
    usoMemoriaDinamica()