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
        self.mostrar()
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]

    def obtenerEliminando (self,pos):
        self.mostrar()
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista[pos]
            # self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux=[]
            for ind in range (pos):
                listaAux == [self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux += [self.lista[indice]]
                self.longitud -= 1
                self.lista = listaAux
            return [self.lista,eliminado]

    def mostrar (self):
        print("{:10}    {}".format("lista","posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}]{:3}".format(ele,pos))

lista1 = lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.append("Milagro")
lista1.mostrar()
posicion = int(input("Ingrese posicion para obtener el elemento:"))
resp = lista1.obtenerEliminando(posicion)
if resp == None:
    print("posicion no valida, verifique la lista porfavor...")
else:
    print("el elemento de la posicion:{} indicada es:{}".format(posicion,resp))