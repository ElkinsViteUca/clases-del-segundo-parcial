class lista:
    def __init__(self,tamanio=3):
        self.lista = [2,4,3]
        self.longitud = 0
        self.size = tamanio 
    
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
        else:
            print("lista esta llena")
    
    def obtener (self,pos):
        pass

    def mostrar (self):
        print("   Lista   Posicion")
        for pos,ele in enumerate(self.lista):
            print("[{:10}]{:3}".format(ele,pos))



lista1 = lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.append("Milagro")
lista1.mostrar()