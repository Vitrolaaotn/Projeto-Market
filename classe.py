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

