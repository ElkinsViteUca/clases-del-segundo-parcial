class matriz:
    def __init__(self,matriz):
        self.matriz = matriz

    def ingrsar (self,dato):
        pass

    def presentar (self):
        for fila in range(len(numeros)):
           columna = numeros[fila]
        for col in range(len(columna)):
                print(columna[col],end=" ")
                print()


   

numeros = [[10,20,30,],[60,80,90],[25,35,55]]

# col= numeros[0]
# print(numeros[0],numeros[0][1])
# print(col,col[1])
mat = matriz(numeros)
mat.presentar()