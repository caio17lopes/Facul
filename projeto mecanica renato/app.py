import customtkinter as ctk
import sqlite3

# Configurações da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cadastro de Serviços - Oficina")
app.geometry("700x700")

# Campos de entrada
entrada_proprietario = ctk.CTkEntry(app, placeholder_text="Nome do proprietário")
entrada_proprietario.pack(pady=5)

entrada_veiculo = ctk.CTkEntry(app, placeholder_text="Veículo")
entrada_veiculo.pack(pady=5)

entrada_fabricante = ctk.CTkEntry(app, placeholder_text="Fabricante")
entrada_fabricante.pack(pady=5)

entrada_ano = ctk.CTkEntry(app, placeholder_text="Ano do veículo")
entrada_ano.pack(pady=5)

entrada_placa = ctk.CTkEntry(app, placeholder_text="Placa")
entrada_placa.pack(pady=5)

entrada_servico = ctk.CTkEntry(app, placeholder_text="Serviço efetuado")
entrada_servico.pack(pady=5)

entrada_pecas = ctk.CTkEntry(app, placeholder_text="Valor das peças")
entrada_pecas.pack(pady=5)

entrada_mao = ctk.CTkEntry(app, placeholder_text="Valor da mão de obra")
entrada_mao.pack(pady=5)

entrada_data = ctk.CTkEntry(app, placeholder_text="Data do serviço (dd/mm/aaaa)")
entrada_data.pack(pady=5)

entrada_obs = ctk.CTkEntry(app, placeholder_text="Observações")
entrada_obs.pack(pady=5)

def salvar():
    con = sqlite3.connect("oficina.db")
    cur = con.cursor()
    cur.execute('''
        INSERT INTO cadastro (
            proprietario, veiculo, fabricante, ano_veiculo, placa,
            servico, valor_pecas, valor_servico, data_servico, observacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        entrada_proprietario.get(),
        entrada_veiculo.get(),
        entrada_fabricante.get(),
        entrada_ano.get(),
        entrada_placa.get(),
        entrada_servico.get(),
        float(entrada_pecas.get()),
        float(entrada_mao.get()),
        entrada_data.get(),
        entrada_obs.get()
    ))
    con.commit()
    con.close()
    print("Cadastro salvo com sucesso!")

botao = ctk.CTkButton(app, text="Salvar Cadastro", command=salvar)
botao.pack(pady=20)
app.mainloop()
