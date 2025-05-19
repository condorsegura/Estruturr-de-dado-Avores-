# Percurso Pre ordem 
# funçao 
def pre_ordem(raiz):
    if raiz is not None:
        print(raiz.valor)
        pre_ordem(raiz.esquerda)
        pre_ordem(raiz.direita)
    else:
        return
    
# Função para percorrer uma árvore binária em ordem (in-order traversal)
def em_ordem(raiz):
    """
    Percorre a árvore binária em ordem (esquerda, raiz, direita) e imprime os valores dos nós.

    Parâmetros:
    raiz -- nó raiz da árvore ou subárvore a ser percorrida

    Funcionamento:
    - Visita recursivamente o filho da esquerda
    - Imprime o valor do nó atual
    - Visita recursivamente o filho da direita
    """
    if raiz is not None:
        em_ordem(raiz.esquerda)   # Percorre a subárvore esquerda
        print(raiz.valor)         # Visita o nó atual
        em_ordem(raiz.direita)    # Percorre a subárvore direita
    else:
        return