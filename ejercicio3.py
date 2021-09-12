class pila:
    def __init__(self,tamanio=1):
        self.lista = []
        self.size = 5
        self.top = 0
    
    def push (self):
        pass

    def pop(self):
        pass

    def show(self):
        pass

    def empty(self):
        if self.top == 0:
            print("Pila esta vacia")

pila1 = pila(5)
print(pila1.size)
pila2 = pila(15)
print(pila2.size)
