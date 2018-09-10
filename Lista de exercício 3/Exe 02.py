'''
Autor: Ana Clara Nunes
Data: 04/06/2018

Enunciado

Questão 2
'''

n1 = float(input('Digite sua primeira nota parcial: '))
n2 = float(input('Digite sua segunda nota parcial: '))

print('Suas notas foram:',n1,'e',n2,)

me = (n1 + n2) / 2
print('Sua média foi:',me,)

if 9.0 <= me <= 10.0:
    print('A - APROVADO')
if 7.5 <= me < 9.0:
    print('B - APROVADO')
if 6.0 <= me < 7.5:
    print('C - APROVADO')
if 4.0 <= me < 6.0:
    print('D - REPROVADO')
if me < 4.0:
    print('E - REPROVADO')
