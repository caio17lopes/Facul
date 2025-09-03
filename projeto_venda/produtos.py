import customtkinter as ctk
from tkinter import messagebox
from db import conectar

class Produtos:
    def __init__(self, master):
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.conn = conectar()

        self.nome = ctk.CTkEntry(self.frame, placeholder_text="Nome do produto")
        self.nome.pack(pady=5)

        self.preco = ctk.CTkEntry(self.frame, placeholder_text="Preço")
        self.preco.pack(pady=5)

        self.btn_salvar = ctk.CTkButton(self.frame, text="Salvar", command=self.salvar)
        self.btn_salvar.pack(pady=5)

        self.label_total = ctk.CTkLabel(self.frame, text="")
        self.label_total.pack(pady=5)

        self.lista_frame = ctk.CTkFrame(self.frame)
        self.lista_frame.pack(pady=10, fill="both", expand=True)

        self.produto_selecionado = None  # Guarda ID do produto em edição

        self.listar()

    def salvar(self):
        nome = self.nome.get()
        preco = self.preco.get()

        if not nome or not preco:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido.")
            return

        cursor = self.conn.cursor()

        if self.produto_selecionado:  # Edição
            cursor.execute("UPDATE produtos SET nome=?, preco=? WHERE id=?", (nome, preco, self.produto_selecionado))
            messagebox.showinfo("Sucesso", "Produto atualizado.")
            self.produto_selecionado = None
            self.btn_salvar.configure(text="Salvar")
        else:  # Novo cadastro
            cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", (nome, preco))
            messagebox.showinfo("Sucesso", "Produto cadastrado.")

        self.conn.commit()
        self.nome.delete(0, 'end')
        self.preco.delete(0, 'end')
        self.listar()

    def listar(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()

        for produto in produtos:
            nome = produto[1]
            preco = produto[2]
            id_produto = produto[0]

            linha = ctk.CTkFrame(self.lista_frame)
            linha.pack(fill="x", pady=2)

            label = ctk.CTkLabel(linha, text=f"{nome} - R$ {preco:.2f}", width=200, anchor="w")
            label.pack(side="left", padx=5)

            btn_editar = ctk.CTkButton(linha, text="✏️", width=30, command=lambda id=id_produto: self.editar(id))
            btn_editar.pack(side="left", padx=2)

            btn_excluir = ctk.CTkButton(linha, text="🗑️", width=30, command=lambda id=id_produto: self.excluir(id))
            btn_excluir.pack(side="left", padx=2)

        self.label_total.configure(text=f"Total de produtos: {len(produtos)}")

    def editar(self, id_produto):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nome, preco FROM produtos WHERE id=?", (id_produto,))
        produto = cursor.fetchone()
        if produto:
            self.nome.delete(0, 'end')
            self.nome.insert(0, produto[0])
            self.preco.delete(0, 'end')
            self.preco.insert(0, str(produto[1]))
            self.produto_selecionado = id_produto
            self.btn_salvar.configure(text="Atualizar")

    def excluir(self, id_produto):
        if messagebox.askyesno("Confirmação", "Deseja realmente excluir este produto?"):
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id=?", (id_produto,))
            self.conn.commit()
            self.listar()
