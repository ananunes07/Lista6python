'''
Autor: Ana Clara Nunes
Data:01/08/2018

Questão 04
'''
p = 0
 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

tu = (n1,n2,n3,n4)

for n in tu:
    if n%2 == 0:
        print('{} é um número par'.format(n))

