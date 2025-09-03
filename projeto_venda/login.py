import customtkinter as ctk
from tkinter import messagebox
from db import conectar
from dashboard import Dashboard

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Login")
        self.conn = conectar()

        self.label = ctk.CTkLabel(self, text="Usuário")
        self.label.pack(pady=5)
        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.pack()

        self.label2 = ctk.CTkLabel(self, text="Senha")
        self.label2.pack(pady=5)
        self.entry_senha = ctk.CTkEntry(self, show="*")
        self.entry_senha.pack()

        self.button = ctk.CTkButton(self, text="Entrar", command=self.login)
        self.button.pack(pady=10)

    def login(self):
        user = self.entry_user.get()
        senha = self.entry_senha.get()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND senha=?", (user, senha))
        if cursor.fetchone():
            self.destroy()
            app = Dashboard()
            app.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
