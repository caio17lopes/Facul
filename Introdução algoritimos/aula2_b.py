'''
Composição com marcodres de posição

Marcador      / Tipo
%d ou %i      / Números inteiros
%f            / Números de pontos flutuante
%s            / Strings
Exemplos:
'''
nota = 8.5
s1 = "Você tirou %f na disciplina de Algoritimos" % nota
print(s1)

# Limitando casas decimais
nota = 8.5
s1 = "Você tirou %.2f na disciplina de Algoritimos" % nota
print(s1)

# Varias variaveis 

nota = 8.5
disciplina = 'Algoritimos'
s1 = "Você tirou %.2f na disciplina de %s" %  (nota , disciplina) 
print(s1)

# Composição moderna
nota = 8.5
disciplina = 'Algoritimos'
s1 = "Você tirou {} na disciplina de {}".format(nota , disciplina) 
print(s1)

# Composição com f-string
nota = 8.5
disciplina = 'Algoritimos'
s1 = f"Você tirou {nota} na disciplina de {disciplina} "  
print(s1)