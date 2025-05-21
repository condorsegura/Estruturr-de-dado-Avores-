# biblioteca bisect
# Funções para manipular uma lista ordenada como se fosse uma árvore de busca

import bisect  # Importa o módulo bisect para inserção ordenada eficiente

class Arvores(object):
    def __init__(self, elementos):
        """
        Inicializa a estrutura com uma lista ordenada.
        Parâmetros:
        - elementos: lista de valores a serem inseridos inicialmente na árvore.
        """
        self.arvore = []  # Cria uma lista vazia para armazenar os elementos
        self.add_elementos(elementos)  # Adiciona os elementos iniciais

    def add_elementos(self, elementos):
        """
        Adiciona vários elementos à árvore.
        Parâmetros:
        - elementos: lista de valores a serem inseridos.
        """
        for i in elementos:
            self.add_elemento(i)  # Usa o método de adicionar elemento individualmente

    def add_elemento(self, elemento):
        """
        Adiciona um elemento à árvore, mantendo a ordem.
        Parâmetros:
        - elemento: valor a ser inserido.
        """
        if elemento not in self.arvore:  # Verifica se o elemento já existe
            bisect.insort(self.arvore, elemento)  # Insere de forma ordenada
        else:
            print("Elemento já existe na árvore")  # Mensagem se o elemento já está presente

    def remove_elemento(self, elemento):
        """
        Remove um elemento da árvore.
        Parâmetros:
        - elemento: valor a ser removido.
        Retorna:
        - False se o elemento não for encontrado, True caso contrário.
        """
        if elemento in self.arvore:  # Verifica se o elemento existe na lista
            try:
                self.arvore.remove(elemento)  # Remove o elemento
            except ValueError:
                print("Elemento não encontrado na árvore")  # Caso raro de erro
                return False
        else:
            print("Elemento não encontrado na árvore")  # Mensagem se não existe
            return False

if __name__ == "__main__":
    # Exemplo de uso da classe Arvores
    arvore = Arvores([1, 2, 3, 4, 5])  # Cria a árvore com elementos iniciais
    print(arvore.arvore)                # Exibe a árvore ordenada
    arvore.add_elemento(6)              # Adiciona o elemento 6
    print(arvore.arvore)                # Exibe a árvore após inserção
    arvore.remove_elemento(3)           # Remove o elemento 3
    print(arvore.arvore)                # Exibe a árvore após remoção