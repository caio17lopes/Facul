#1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra que é vogal ou consoante: ')
if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u' or \
    letra == 'A' or letra == 'E' or letra == 'I' or letra == 'U'):
    print(f'A Letra que você digitou é: "{letra}" uma vogal')
else:
    print(f'A Letra que você digitou é: {letra} uma consoante ')

'''2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

media1 = float(input('Informe a primeira nota do aluno: '))
media2 = float(input('Informe a segunda nota do aluno: '))

total_media = (media1 + media2) /2

if total_media == 10:
    print(f'Aprovado com honras, sua nota foi {total_media}')

elif total_media < 7:
    print(f'Reprovado, sua media foi de {total_media}')
else:
    print(f'Aprovado, sua media foi de {total_media}')

'''

'''