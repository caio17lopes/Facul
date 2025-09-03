# app.py
import customtkinter as ctk
import sqlite3

# Criação do banco
def criar_banco():
    con = sqlite3.connect("oficina.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            proprietario TEXT,
            veiculo TEXT,
            fabricante TEXT,
            ano_veiculo TEXT,
            placa TEXT,
            servico TEXT,
            valor_pecas REAL,
            valor_servico REAL,
            valor_total REAL,
            data_servico TEXT,
            observacao TEXT
        )
    ''')
    con.commit()
    con.close()

criar_banco()

# Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x600")
app.title("Sistema Oficina")

frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)

def limpar_tela():
    for widget in frame_principal.winfo_children():
        widget.destroy()

def tela_menu():
    limpar_tela()
    ctk.CTkLabel(frame_principal, text="Menu Principal", font=("Arial", 22)).pack(pady=20)
    ctk.CTkButton(frame_principal, text="Cadastrar Serviço", width=200, command=tela_cadastro).pack(pady=10)
    ctk.CTkButton(frame_principal, text="Ver Cadastros", width=200, command=tela_listagem).pack(pady=10)

def tela_cadastro():
    limpar_tela()
    ctk.CTkLabel(frame_principal, text="Cadastro de Serviço", font=("Arial", 20)).pack(pady=10)

    entradas = {}
    campos = [
        ("proprietario", "Nome do proprietário"),
        ("veiculo", "Veículo"),
        ("fabricante", "Fabricante"),
        ("ano_veiculo", "Ano do veículo"),
        ("placa", "Placa"),
        ("servico", "Serviço realizado"),
        ("valor_pecas", "Valor das peças"),
        ("valor_servico", "Valor da mão de obra"),
        ("data_servico", "Data do serviço"),
        ("observacao", "Observações")
    ]

    for chave, texto in campos:
        entradas[chave] = ctk.CTkEntry(frame_principal, placeholder_text=texto)
        entradas[chave].pack(pady=3)

    def salvar():
        try:
            pecas = float(entradas["valor_pecas"].get())
            servico = float(entradas["valor_servico"].get())
            total = pecas + servico

            dados = (
                entradas["proprietario"].get(),
                entradas["veiculo"].get(),
                entradas["fabricante"].get(),
                entradas["ano_veiculo"].get(),
                entradas["placa"].get(),
                entradas["servico"].get(),
                pecas,
                servico,
                total,
                entradas["data_servico"].get(),
                entradas["observacao"].get()
            )

            con = sqlite3.connect("oficina.db")
            cur = con.cursor()
            cur.execute('''
                INSERT INTO cadastro (
                    proprietario, veiculo, fabricante, ano_veiculo, placa,
                    servico, valor_pecas, valor_servico, valor_total, data_servico, observacao
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', dados)
            con.commit()
            con.close()
            tela_menu()
        except ValueError:
            ctk.CTkLabel(frame_principal, text="Erro: Verifique os valores numéricos.").pack()

    ctk.CTkButton(frame_principal, text="Salvar", command=salvar).pack(pady=10)
    ctk.CTkButton(frame_principal, text="Voltar", command=tela_menu).pack(pady=10)

def tela_listagem():
    limpar_tela()
    ctk.CTkLabel(frame_principal, text="Registros Cadastrados", font=("Arial", 20)).pack(pady=10)

    con = sqlite3.connect("oficina.db")
    cur = con.cursor()
    cur.execute("SELECT id, proprietario, veiculo, placa, valor_total FROM cadastro")
    registros = cur.fetchall()
    con.close()

    for reg in registros:
        texto = f"ID: {reg[0]} | {reg[1]} - {reg[2]} | Placa: {reg[3]} | Total: R$ {reg[4]:.2f}"
        ctk.CTkLabel(frame_principal, text=texto).pack(pady=2)

    ctk.CTkButton(frame_principal, text="Voltar", command=tela_menu).pack(pady=20)

tela_menu()
app.mainloop()
