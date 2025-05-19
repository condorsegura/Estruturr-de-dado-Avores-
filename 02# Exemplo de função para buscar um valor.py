# Exemplo de função para buscar um valor em uma árvore binária de busca

class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def buscar(raiz, valor):
    """
    Busca um valor em uma árvore binária de busca.
    
    Parâmetros:
    raiz  -- nó raiz da árvore (ou subárvore) onde a busca começa
    valor -- valor a ser procurado na árvore

    Retorno:
    O nó que contém o valor, ou None se não encontrado.
    """
    # Se a árvore está vazia ou chegou em uma folha sem encontrar o valor
    if raiz is None:
        return None
    # Se encontrou o valor no nó atual
    if raiz.chave == valor:
        return raiz
    # Se o valor procurado é menor, busca na subárvore esquerda
    if valor < raiz.chave:
        return buscar(raiz.esquerda, valor)
    # Se o valor procurado é maior, busca na subárvore direita
    else:
        return buscar(raiz.direita, valor)

# Exemplo de uso:
if __name__ == "__main__":
    # Criando os nós da árvore
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)
    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)
    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)

    # Buscando um valor na árvore
    resultado = buscar(raiz, 65)
    if resultado:
        print(f"Valor {resultado.chave} encontrado na árvore.")
    else:
        print("Valor não encontrado na árvore.")