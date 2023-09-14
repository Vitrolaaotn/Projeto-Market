import os

def parar():
    os.system('pause')

def limpar():
    os.system('cls')

class Carrinho_Compras:
    lista_compra = []

    
    def inserir_produto(self, produto):
        self.produto = produto
        self.lista_compra.append(self.produto)

    
    def listar_produtos(self):
        self.cont = 0
        for produto in self.lista_compra:
            self.cont += 1
            print(f"{self.cont} -> Nome: {produto.getNome()}, Valor: {produto.getValor()}")


    def getLista(self, vetor):
        return self.lista_compra[vetor]
    

    def delProduto(self, vetor):
        self.vetor_lista = vetor - 1
        self.lista_compra.pop(self.vetor_lista)


class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def getNome(self):
        return self.nome

    def getValor(self):
        return self.valor

    def setNome(self, nome):
        self.nome = nome

    def setValor(self, valor):
        self.valor = valor