"""
OPERADORES ARITIMÉTICOS
Python      / Operação

+           / adição
-           / subtração
*           / multiplicação
/           / divisão               
//          / divisão somente a parte inteira 
%           / modulos, resto da divisão 
**          / exponenciação ou potenciação

OPERADORES RELACIONAIS

==          /   igualdade
>           /   maior que
<           /   menor que
>=          /   maior ou igual
<=          /   menor ou igual
!=          /   diferente

OPERADORES LOGIOCS

not         /   não     /   negação
and         /   e       /   conjunção       
or          /   or      /   disjunção


"""
'''
OPERADORES ESPECIAIS DE ATRIBUIÇÃO

OPERADOR    /   EXEMPLO     /       EQUIVALENTE
+=          /   x += 1      /       x = x + 1
-=          /   x -= 1      /       x = x - 1
*=          /   x *= 2      /       x = x * 2       
/=          /   x /= 2      /       x = x / 2
**=         /   x **= 2     /       x = x ** 2
//          /   x //= 2     /       x = x // 2
'''
from datetime import datetime

data_atual = datetime.now()
print(data_atual.date())


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys

class MeuApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha GUI com PyQt")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Olá, mundo!")
        layout.addWidget(self.label)

        botao = QPushButton("Clique em mim")
        botao.clicked.connect(self.mudar_texto)
        layout.addWidget(botao)

        self.setLayout(layout)

    def mudar_texto(self):
        self.label.setText("Botão clicado!")

app = QApplication(sys.argv)
janela = MeuApp()
janela.show()
sys.exit(app.exec())