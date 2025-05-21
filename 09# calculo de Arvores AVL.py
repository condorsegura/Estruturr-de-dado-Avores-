# calculo de Arvores AVL

class NoAVL:
    """
    Classe que representa um nó de uma árvore AVL.
    Cada nó possui uma chave, ponteiros para os filhos esquerdo e direito e altura.
    """
    def __init__(self, chave):
        self.chave = chave           # Valor armazenado no nó
        self.esquerda = None         # Ponteiro para o filho à esquerda
        self.direita = None          # Ponteiro para o filho à direita
        self.altura = 1              # Altura do nó (inicialmente 1)

def altura(no):
    """
    Retorna a altura de um nó.
    Se o nó for None, retorna 0.
    Parâmetros:
    - no: nó da árvore AVL
    Retorno:
    - altura do nó (int)
    """
    if no is None:
        return 0
    return no.altura

def fator_balanceamento(no):
    """
    Calcula e retorna o fator de balanceamento de um nó.
    Parâmetros:
    - no: nó da árvore AVL
    Retorno:
    - diferença entre altura da subárvore esquerda e direita (int)
    """
    if no is None:
        return 0
    return altura(no.esquerda) - altura(no.direita)

def rotacao_direita(y):
    """
    Realiza uma rotação simples à direita e retorna o novo nó raiz.
    Parâmetros:
    - y: nó desbalanceado
    Retorno:
    - novo nó raiz após rotação (NoAVL)
    """
    x = y.esquerda
    T2 = x.direita

    # Rotação propriamente dita
    x.direita = y
    y.esquerda = T2

    # Atualiza alturas dos nós envolvidos
    y.altura = 1 + max(altura(y.esquerda), altura(y.direita))
    x.altura = 1 + max(altura(x.esquerda), altura(x.direita))

    return x

def rotacao_esquerda(x):
    """
    Realiza uma rotação simples à esquerda e retorna o novo nó raiz.
    Parâmetros:
    - x: nó desbalanceado
    Retorno:
    - novo nó raiz após rotação (NoAVL)
    """
    y = x.direita
    T2 = y.esquerda

    # Rotação propriamente dita
    y.esquerda = x
    x.direita = T2

    # Atualiza alturas dos nós envolvidos
    x.altura = 1 + max(altura(x.esquerda), altura(x.direita))
    y.altura = 1 + max(altura(y.esquerda), altura(y.direita))

    return y

def inserir(no, chave):
    """
    Insere uma chave na árvore AVL e retorna o novo nó raiz.
    Parâmetros:
    - no: nó raiz da árvore/subárvore
    - chave: valor a ser inserido
    Retorno:
    - novo nó raiz após inserção e balanceamento (NoAVL)
    """
    # 1. Inserção normal em árvore binária de busca
    if no is None:
        return NoAVL(chave)
    elif chave < no.chave:
        no.esquerda = inserir(no.esquerda, chave)
    elif chave > no.chave:
        no.direita = inserir(no.direita, chave)
    else:
        # Chaves duplicadas não são permitidas
        return no

    # 2. Atualiza altura do nó atual
    no.altura = 1 + max(altura(no.esquerda), altura(no.direita))

    # 3. Calcula o fator de balanceamento
    balance = fator_balanceamento(no)

    # 4. Realiza rotações se necessário

    # Caso Esquerda-Esquerda
    if balance > 1 and chave < no.esquerda.chave:
        return rotacao_direita(no)

    # Caso Direita-Direita
    if balance < -1 and chave > no.direita.chave:
        return rotacao_esquerda(no)

    # Caso Esquerda-Direita
    if balance > 1 and chave > no.esquerda.chave:
        no.esquerda = rotacao_esquerda(no.esquerda)
        return rotacao_direita(no)

    # Caso Direita-Esquerda
    if balance < -1 and chave < no.direita.chave:
        no.direita = rotacao_direita(no.direita)
        return rotacao_esquerda(no)

    return no

def em_ordem(no):
    """
    Percorre a árvore em ordem e imprime as chaves.
    Parâmetros:
    - no: nó raiz da árvore/subárvore
    """
    if no is not None:
        em_ordem(no.esquerda)
        print(no.chave, end=' ')
        em_ordem(no.direita)

# Exemplo de uso:
if __name__ == "__main__":
    # Cria uma árvore AVL e insere valores
    raiz = None
    valores = [30, 20, 40, 10, 25, 35, 50, 5]
    for v in valores:
        raiz = inserir(raiz, v)
    print("Árvore AVL em ordem:")
    em_ordem(raiz)
    print()