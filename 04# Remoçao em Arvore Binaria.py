# Remoçao em Arvore Binaria 
# funçao remove

def remove(raiz, valor):
    if raiz is None:
        return raiz

    # Se o valor a ser removido é menor que o valor da raiz,
    # então ele está na subárvore esquerda
    if valor < raiz.valor:
        raiz.esquerda = remove(raiz.esquerda, valor)

    # Se o valor a ser removido é maior que o valor da raiz,
    # então ele está na subárvore direita
    elif valor > raiz.valor:
        raiz.direita = remove(raiz.direita, valor)

    # Se o valor é igual ao valor da raiz, então este é o nó a ser removido
    else:
        # Caso 1: nó com apenas um filho ou nenhum filho
        if raiz.esquerda is None:
            return raiz.direita
        elif raiz.direita is None:
            return raiz.esquerda

        
