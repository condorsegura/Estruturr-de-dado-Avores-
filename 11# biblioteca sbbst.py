# biblioteca sbbst
# Exemplo de uso de uma árvore de busca binária auto-balanceada (SBBST)

from sbbst import sbbst  # Importa a classe sbbst de um módulo externo

# Teste de inserção e busca em uma árvore SBBST
tree = sbbst()  # Cria uma nova árvore SBBST vazia

# Lista de números a serem inseridos na árvore
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for num in nums:
    tree.insert(num)  # Insere o número na árvore

    # Exibe informações sobre a árvore após cada inserção
    print("Número de elementos:", tree.getSize())           # Tamanho da árvore
    print("Altura:", tree.getHeightTree())                  # Altura da árvore
    print("Menor valor:", tree.getMinVal())               # Menor valor na árvore
    print("Maior valor:", tree.getMaxVal())               # Maior valor na árvore
    print("3º menor valor:", tree.kthsmallest(3))           # 3º menor valor
    print("2º maior valor:", tree.kthlargest(2))            # 2º maior valor
    print("Em ordem:", tree.inOrder())                      # Percurso em ordem
    print("Pré-ordem:", tree.preOrder())                    # Percurso pré-ordem
    print("Pós-ordem:", tree.postOrder())                   # Percurso pós-ordem

    # Remove o número da árvore duas vezes (a segunda chamada não terá efeito se já foi removido)
    tree.delete(num)
    tree.delete(num)

# ----------------------------------------------------------
# Exemplo similar usando apenas listas para simular operações básicas

class SimulaArvore:
    """
    Classe para simular operações básicas de uma árvore de busca usando lista ordenada.
    """
    def __init__(self):
        self.dados = []

    def insert(self, valor):
        if valor not in self.dados:
            self.dados.append(valor)
            self.dados.sort()

    def delete(self, valor):
        if valor in self.dados:
            self.dados.remove(valor)

    def getsize(self):
        return len(self.dados)

    def getHeightTree(self):
        # Altura mínima de uma árvore balanceada: log2(n+1)
        import math
        if not self.dados:
            return 0
        return int(math.log2(len(self.dados) + 1))

    def getMinValue(self):
        return self.dados[0] if self.dados else None

    def getMaxValue(self):
        return self.dados[-1] if self.dados else None

    def kthsmallest(self, k):
        if 0 < k <= len(self.dados):
            return self.dados[k-1]
        return None

    def kthlargest(self, k):
        if 0 < k <= len(self.dados):
            return self.dados[-k]
        return None

    def inOrder(self):
        return self.dados.copy()

    def preOrder(self):
        # Para simulação, retorna a lista (não é o real percurso pré-ordem)
        return self.dados.copy()

    def postOrder(self):
        # Para simulação, retorna a lista invertida (não é o real percurso pós-ordem)
        return self.dados[::-1]

# Exemplo de uso da classe simulada
print("\n--- Simulação com lista ordenada ---")
sim_tree = SimulaArvore()
for num in nums:
    sim_tree.insert(num)
    print("Número de elementos:", sim_tree.getsize())
    print("Altura:", sim_tree.getHeightTree())
    print("Menor valor:", sim_tree.getMinValue())
    print("Maior valor:", sim_tree.getMaxValue())
    print("3º menor valor:", sim_tree.kthsmallest(3))
    print("2º maior valor:", sim_tree.kthlargest(2))
    print("Em ordem:", sim_tree.inOrder())
    print("Pré-ordem:", sim_tree.preOrder())
    print("Pós-ordem:", sim_tree.postOrder())
    sim_tree.delete(num)
    sim_tree.delete(num)