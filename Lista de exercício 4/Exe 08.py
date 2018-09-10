'''
Autor: Ana Clara Nunes
Data: 12/07/2018

Questão 08
'''

a = 800000
b = 2000000

anos = 0

while True:
    anos += 1
    a = a + a*0.03
    b = b + b*0.015
    if a >= b:
        break

print('Foram necessarios {} anos para o pais / A passar o pais B'.format(anos))
