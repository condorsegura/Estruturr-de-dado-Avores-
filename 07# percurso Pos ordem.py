# percurso Pos ordem 
#funçao 
def percurso_pos_ordem(raiz):
    if raiz is not None:
        percurso_pos_ordem(raiz.esquerda)
        percurso_pos_ordem(raiz.direita)
        print(raiz.valor, end=' ')

# Função para percorrer uma árvore binária em ordem simétrica (in-order traversal)
def percurso_em_ordem(raiz):
    """
    Percorre a árvore binária em ordem simétrica (esquerda, raiz, direita) e imprime os valores dos nós.

    Parâmetros:
    raiz -- nó raiz da árvore ou subárvore a ser percorrida

    Funcionamento:
    - Visita recursivamente o filho da esquerda
    - Imprime o valor do nó atual
    - Visita recursivamente o filho da direita
    """
    if raiz is not None:
        percurso_em_ordem(raiz.esquerda)   # Percorre a subárvore esquerda
        print(raiz.valor, end=' ')         # Visita o nó atual
        percurso_em_ordem(raiz.direita)    # Percorre a subárvore direita