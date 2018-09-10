'''
Autor: Ana Clara Nunes
Data: 20/06/2018

Questão 04
'''

n = int(input('Digite o número inteiro não negativo: '))

fa = 1
for x in range(2,n+1):
    fa = fa * x
print('O fatoral deste número é:',fa)
    
    
