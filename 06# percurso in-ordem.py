# percurso in-ordem 
# funçao
def in_ordem(raiz):
    if raiz != None:
        in_ordem(raiz.esquerda)
        print(raiz.valor)
        in_ordem(raiz.direita)
# Função para percorrer uma árvore binária em pré-ordem (pre-order traversal)
def pre_ordem(raiz):
    """
    Percorre a árvore binária em pré-ordem (raiz, esquerda, direita) e imprime os valores dos nós.

    Parâmetros:
    raiz -- nó raiz da árvore ou subárvore a ser percorrida

    Funcionamento:
    - Imprime o valor do nó atual
    - Visita recursivamente o filho da esquerda
    - Visita recursivamente o filho da direita
    """
    if raiz is not None:
        print(raiz.valor)           # Visita o nó atual (raiz)
        pre_ordem(raiz.esquerda)    # Percorre a subárvore esquerda
        pre_ordem(raiz.direita)     # Percorre a subárvore direita