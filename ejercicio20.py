class matriz:
    def __init__(self,matriz):
        self.matriz = matriz

    def ingrsar (self,dato):
        pass

    def presentar (self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
                print()

    def buscar(self,valor):
        enc = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col]==valor:
                    enc["fila"]=fila
                    enc["col"]=col
                    break
                if enc: break
            return enc



   

numeros = [[10,20,30,],[60,80,90],[25,35,55]]

# col= numeros[0]
# print(numeros[0],numeros[0][1])
# print(col,col[1])
mat = matriz(numeros)
mat.presentar()