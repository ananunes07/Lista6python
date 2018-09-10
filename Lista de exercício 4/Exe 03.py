'''

Autor: Ana Clara Nunes
Data: 18/06/2018

Questão 03

'''
maior = 0
menor = 999999999999999999999
x = 1
while x != 0:
    n = int(input('Digite o número:'))
    if n == 0:
        break
    if n > maior:
        maior = n
    if n < menor:
        menor = n
        
print('O maior número é:',maior)
print('O menor número é:',menor)
