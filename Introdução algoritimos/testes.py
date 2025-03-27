import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importando ttk para o Treeview

# Dados simulados do banco
banco_de_dados = {
    'cadastro': {
        'id': [],
        'proprietario': [],
        'veiculo': [],
        'fabricante': [],
        'ano_veiculo': [],
        'placa': [],
        'servico': [],
        'valor_pecas': [],
        'valor_servico': [],
        'data_servico': [],
        'observacao': []
    }
}

# Função para adicionar um cadastro
def adicionar_cadastro():
    # Recupera as informações do formulário
    proprietario = entry_proprietario.get().title()
    veiculo = entry_veiculo.get().upper()
    fabricante = entry_fabricante.get().upper()
    ano_veiculo = entry_ano.get()
    placa = entry_placa.get().upper()
    servico = entry_servico.get()
    try:
        valor_pecas = float(entry_valor_pecas.get())
        valor_servico = float(entry_valor_servico.get())
    except ValueError:
        messagebox.showerror("Erro", "Os valores das peças e do serviço devem ser números!")
        return
    data_servico = entry_data.get()
    observacao = entry_observacao.get()

    # Adiciona os dados ao banco_de_dados
    id_cliente = len(banco_de_dados['cadastro']['id']) + 1  # Gera ID
    dados = [id_cliente, proprietario, veiculo, fabricante, ano_veiculo, placa, servico, valor_pecas, valor_servico, data_servico, observacao]
    for chave, valor in zip(banco_de_dados['cadastro'].keys(), dados):
        banco_de_dados['cadastro'][chave].append(valor)

    # Limpa os campos
    limpar_campos()

    # Atualiza a exibição dos clientes cadastrados
    atualizar_exibicao()

# Função para limpar os campos de entrada
def limpar_campos():
    entry_proprietario.delete(0, tk.END)
    entry_veiculo.delete(0, tk.END)
    entry_fabricante.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_placa.delete(0, tk.END)
    entry_servico.delete(0, tk.END)
    entry_valor_pecas.delete(0, tk.END)
    entry_valor_servico.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_observacao.delete(0, tk.END)

# Função para atualizar a exibição dos cadastros
def atualizar_exibicao():
    # Limpa a área de exibição atual
    for row in tree.get_children():
        tree.delete(row)

    # Exibe os cadastros no Treeview
    for i, dados in enumerate(zip(*[banco_de_dados['cadastro'][chave] for chave in banco_de_dados['cadastro']])):
        tree.insert('', 'end', values=dados)

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Clientes - Mecânica")

# Criação dos campos de entrada
tk.Label(root, text="Nome do Proprietário:").grid(row=0, column=0, padx=10, pady=5)
entry_proprietario = tk.Entry(root)
entry_proprietario.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nome do Veículo:").grid(row=1, column=0, padx=10, pady=5)
entry_veiculo = tk.Entry(root)
entry_veiculo.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Fabricante:").grid(row=2, column=0, padx=10, pady=5)
entry_fabricante = tk.Entry(root)
entry_fabricante.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Ano do Veículo:").grid(row=3, column=0, padx=10, pady=5)
entry_ano = tk.Entry(root)
entry_ano.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Placa do Veículo:").grid(row=4, column=0, padx=10, pady=5)
entry_placa = tk.Entry(root)
entry_placa.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Serviço Efetuado:").grid(row=5, column=0, padx=10, pady=5)
entry_servico = tk.Entry(root)
entry_servico.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Valor das Peças:").grid(row=6, column=0, padx=10, pady=5)
entry_valor_pecas = tk.Entry(root)
entry_valor_pecas.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Valor do Serviço:").grid(row=7, column=0, padx=10, pady=5)
entry_valor_servico = tk.Entry(root)
entry_valor_servico.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Data do Serviço:").grid(row=8, column=0, padx=10, pady=5)
entry_data = tk.Entry(root)
entry_data.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Observações:").grid(row=9, column=0, padx=10, pady=5)
entry_observacao = tk.Entry(root)
entry_observacao.grid(row=9, column=1, padx=10, pady=5)

# Botão para adicionar cadastro
btn_adicionar = tk.Button(root, text="Adicionar Cadastro", command=adicionar_cadastro)
btn_adicionar.grid(row=10, column=0, columnspan=2, pady=10)

# Criação da tabela para exibir os cadastros usando ttk
tree = ttk.Treeview(root, columns=("ID", "Proprietário", "Veículo", "Fabricante", "Ano", "Placa", "Serviço", "Valor Peças", "Valor Serviço", "Data", "Observações"), show="headings")
tree.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

# Definindo as colunas da tabela
for col in tree["columns"]:
    tree.heading(col, text=col)

# Iniciar a exibição
atualizar_exibicao()

# Iniciar a interface gráfica
root.mainloop()


