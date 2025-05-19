# exemplo de classe de arvores binaria 

class NoArvore:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
        
if __name__ == "__main__":
    # Criando os nós da árvore
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)


