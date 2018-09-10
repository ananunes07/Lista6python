'''
Autor: Ana Clara Nunes
Data:01/08/2018

Questão 06
'''
tupla = ('Bolacha','Cafe','Mandioca','Abacate')

for x in tupla:
    print('As vogais da palavra {} são:'.format(x),end='-')
    for letra in x:
        if letra in 'aeiou':
            print(letra,end='-')
    print()
