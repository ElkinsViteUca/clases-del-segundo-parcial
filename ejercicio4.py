class pila:
    def __init__(self,tamanio=1):
        self.lista = []
        self.size = tamanio
        self.top = 0
    
    def push (self,dato):
        if self.top < self.size:
            self.lista = self.lista + [dato]
            self.top += 1
        else:
            print("La lista ests llena")

    def pop(self):
        pass

    def show(self):
        pass

    def empty(self):
        if self.top == 0:
            print("Pila esta vacia")

pila1 = pila(3)
pila1.push(8)
pila1.push(10)
pila1.push(12)
pila1.push(4)



