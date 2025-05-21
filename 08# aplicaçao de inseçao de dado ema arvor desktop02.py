# aplicaçao de inseçao de dado ema arvore 

import tkinter as tk
from tkinter import messagebox, ttk

# Classe do nó da árvore binária de busca
class NoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

# Função para inserir um valor na árvore binária de busca
def inserir(raiz, valor):
    if raiz is None:
        return NoArvore(valor)
    if valor < raiz.chave:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    elif valor > raiz.chave:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

# Função para percorrer a árvore em ordem e retornar os valores em lista
def em_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz:
        em_ordem(raiz.esquerda, resultado)
        resultado.append(raiz.chave)
        em_ordem(raiz.direita, resultado)
    return resultado

# Função para escolher a melhor raiz (mediana)
def melhor_raiz(valores):
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    if n == 0:
        return None
    return valores_ordenados[n // 2]

# Função para montar a árvore automaticamente com a melhor raiz
def montar_arvore(valores):
    if not valores:
        return None
    raiz_valor = melhor_raiz(valores)
    raiz = NoArvore(raiz_valor)
    for v in valores:
        if v != raiz_valor:
            inserir(raiz, v)
    return raiz

# Função para gerar relatório da árvore
def relatorio_arvore(raiz):
    valores = em_ordem(raiz)
    return (
        f"Relatório da Árvore Binária de Busca\n"
        f"-----------------------------------\n"
        f"Raiz escolhida: {raiz.chave if raiz else 'Nenhuma'}\n"
        f"Valores em ordem: {valores}\n"
        f"Quantidade de nós: {len(valores)}\n"
        f"Menor valor: {min(valores) if valores else 'N/A'}\n"
        f"Maior valor: {max(valores) if valores else 'N/A'}\n"
    )

# Interface gráfica
class AppArvoreDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Árvore Binária Inteligente - Dashboard")
        self.valores = []

        # Entrada de número
        tk.Label(master, text="Digite um número:").pack()
        self.entrada = tk.Entry(master)
        self.entrada.pack()
        tk.Button(master, text="Adicionar Número", command=self.adicionar_numero).pack(pady=5)

        # Lista de números inseridos
        tk.Label(master, text="Números inseridos:").pack()
        self.lista_numeros = tk.Label(master, text="[]")
        self.lista_numeros.pack()

        # Botão para montar árvore e mostrar relatório
        tk.Button(master, text="Montar Árvore e Gerar Relatório", command=self.gerar_relatorio).pack(pady=10)

        # Dashboard/Relatório
        tk.Label(master, text="Dashboard da Árvore:").pack()
        self.texto_relatorio = tk.Text(master, height=10, width=50)
        self.texto_relatorio.pack()

    def adicionar_numero(self):
        try:
            valor = int(self.entrada.get())
            if valor in self.valores:
                messagebox.showwarning("Aviso", "Número já inserido!")
                return
            self.valores.append(valor)
            self.lista_numeros.config(text=str(sorted(self.valores)))
            self.entrada.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro válido.")

    def gerar_relatorio(self):
        if not self.valores:
            messagebox.showwarning("Aviso", "Adicione pelo menos um número.")
            return
        arvore = montar_arvore(self.valores)
        relatorio = relatorio_arvore(arvore)
        self.texto_relatorio.delete(1.0, tk.END)
        self.texto_relatorio.insert(tk.END, relatorio)

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = AppArvoreDashboard(root)
    root.mainloop()