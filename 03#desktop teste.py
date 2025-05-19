import tkinter as tk
from tkinter import messagebox

# Classe do nó da árvore binária
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

# Função para buscar um valor na árvore binária de busca
def buscar(raiz, valor):
    if raiz is None:
        return None
    if raiz.chave == valor:
        return raiz
    if valor < raiz.chave:
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)

# Interface gráfica
class AppArvore:
    def __init__(self, master):
        self.master = master
        master.title("Busca em Árvore Binária")

        self.raiz = None  # Raiz da árvore

        # Entrada para inserir valores
        tk.Label(master, text="Valor para inserir:").pack()
        self.entrada_inserir = tk.Entry(master)
        self.entrada_inserir.pack()
        tk.Button(master, text="Inserir", command=self.inserir_valor).pack(pady=5)

        # Entrada para buscar valores
        tk.Label(master, text="Valor para buscar:").pack()
        self.entrada_buscar = tk.Entry(master)
        self.entrada_buscar.pack()
        tk.Button(master, text="Buscar", command=self.buscar_valor).pack(pady=5)

    def inserir_valor(self):
        try:
            valor = int(self.entrada_inserir.get())
            self.raiz = inserir(self.raiz, valor)
            messagebox.showinfo("Inserção", f"Valor {valor} inserido na árvore.")
            self.entrada_inserir.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro para inserir.")

    def buscar_valor(self):
        try:
            valor = int(self.entrada_buscar.get())
            resultado = buscar(self.raiz, valor)
            if resultado:
                messagebox.showinfo("Busca", f"Valor {valor} encontrado na árvore.")
            else:
                messagebox.showinfo("Busca", f"Valor {valor} NÃO encontrado na árvore.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número inteiro para buscar.")

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = AppArvore(root)
    root.mainloop()