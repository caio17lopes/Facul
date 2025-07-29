# criação calcul ode materias para o meu serviço 

# Criar função para armazenar dados e valores ja 

from tkinter import *



eucafloor = {
    'eucafloor':{
        # Valores já inclusos o lucro 
        'prime_cola': [67.20],
        'prime_click': [75.20],
        'evidence' : [90.00],
        'rodape_7cm': [35.00],
        'rodape_10cm':[44.80],
        'perfil_t': [75.00],
        'perfil_redutor': [75.00],
        'manta':[6.00]
        }
    }   

def venda():
    metragem = float(input('Informe o m² da área: '))
    print('-*-'*20)
    perca = float (input('Infome a quantidade de perca para calculo: '))
    area = ((metragem * perca)/100) + metragem
    print('----#'*20)
    print(f'A area informada foi de {metragem:.2f} , a porcetagem de perca foi de {perca:.2f}, o total da area foi de {area:.2f}')
    print('----#'*20, '\n')
    return area

def acessorios():
    piso = input('Informe qual o piso escolhido: ').strip().upper()
    rodape = input('Infomre se vai ser o rodapé de 7cm ou de 10 cm')
    perfil_t = int(input('Informe a quantidade de perfil T: '))
    perfil_r = int(input('Informe a quantidade de perfil redutor: '))
    manta = int(input('Informe a quantidade de manta: '))

mostrar = eucafloor


janela = Tk()

janela.title('Sistema de estoque')
texto_orientacao = Label(janela, text= 'Valores dos produtos')
texto_orientacao.grid (column=0, row=0)

botao = Button(janela, text = 'Valores dos materiais', command= mostrar)
botao.grid(column=0, row=1)
texto_euca = Label(janela, text='')
texto_euca.grid(column=0 ,row=2)

janela.mainloop()