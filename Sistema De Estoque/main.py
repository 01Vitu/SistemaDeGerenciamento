import tkinter as tk

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

class SistemaEstoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)

    def atualizar_produto(self, nome, quantidade, preco):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.quantidade = quantidade
                produto.preco = preco

    def salvar_arquivo(self):
        arquivo = open("estoque.txt", "w")
        for produto in self.produtos:
            arquivo.write("Nome: {}\nQuantidade: {}\nPreço: {}\n\n".format(produto.nome, produto.quantidade, produto.preco))
        arquivo.close()

class JanelaEstoque(tk.Tk):
    def __init__(self, sistema_estoque):
        tk.Tk.__init__(self)
        self.sistema_estoque = sistema_estoque
        self.title("Sistema de Estoque")

        tk.Label(self, text="Nome").grid(row=0, column=0)
        tk.Label(self, text="Quantidade").grid(row=1, column=0)
        tk.Label(self, text="Preço").grid(row=2, column=0)

        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1)

        self.entry_quantidade = tk.Entry(self)
        self.entry_quantidade.grid(row=1, column=1)

        self.entry_preco = tk.Entry(self)
        self.entry_preco.grid(row=2, column=1)

        tk.Button(self, text="Adicionar", command=self.adicionar_produto).grid(row=3, column=0)
        tk.Button(self, text="Remover", command=self.remover_produto).grid(row=3, column=1)
        tk.Button(self, text="Atualizar", command=self.atualizar_produto).grid(row=3, column=2)
        tk.Button(self, text="Salvar", command=self.salvar_arquivo).grid(row=4, column=1)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())

        produto = Produto(nome, quantidade, preco)
        self.sistema_estoque.adicionar_produto(produto)

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def remover_produto(self):
        nome = self.entry_nome.get()
        self.sistema_estoque.remover_produto(nome)

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def atualizar_produto(self):
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())

        self.sistema_estoque.atualizar_produto(nome, quantidade, preco)

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def salvar_arquivo(self):
        self.sistema_estoque.salvar_arquivo()

sistema_estoque = SistemaEstoque()
janela = JanelaEstoque(sistema_estoque)
janela.mainloop()

