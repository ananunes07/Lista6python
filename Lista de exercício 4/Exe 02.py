'''

Autor: Ana Clara Nunes
Data: 18/06/2018

Questão 02

'''

q = int(input('Quantos produtos você irá comprar:'))

soma = 0
for x in range(1,q+1):
    quant = float(input('Digite o valor do produto:'))
    
    soma += quant
print('A soma dos produtos foi:',soma)
