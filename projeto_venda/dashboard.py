import customtkinter as ctk
from produtos import Produtos

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Painel Principal")

        self.grid_columnconfigure(1, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        
        self.btn_produtos = ctk.CTkButton(self.sidebar, text="Produtos", command=self.abrir_produtos)
        self.btn_produtos.pack(pady=10)

        self.content = ctk.CTkFrame(self)
        self.content.grid(row=0, column=1, sticky="nsew")

    def abrir_produtos(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        Produtos(self.content)
