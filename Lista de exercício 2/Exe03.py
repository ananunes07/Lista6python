'''
Autor: Ana Clara Nunes
Data: 15/05/2018

Enunciado:

Questão 3
'''
p = float(input('Quantos quilos de peixe você pescou: '))

if (p<=50):
    print('O valor da multa é 0')
if (p>50):
    m = (p - 50) * 4
    print('O valor da multa é',m,)
