'''
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

•	Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
•	Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
•	Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
•	Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

•	Se número de páginas for menor que 20 retornar o número de página sem desconto;
•	Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
•	Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
•	Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
•	Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

♦	Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
♦	Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;
♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:

total = (servico * num_pagina) + extra

'''