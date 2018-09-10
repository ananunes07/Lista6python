'''
Autor: Ana Clara Nunes
Data: 15/05/2018

Enunciado:

Questão 4
'''

n1 = float(input('Digite um número:' ))
n2 = float(input('Digite outro um número:' ))
n3 = float(input('Digite outro um número:' ))

if (n1 >= n2):
    if (n1 >= n3):
        print('O número',n1,'é o maior')
else:
    if (n2 >= n1):
        if (n2 >= n3):
            print('O número',n2,'é o maior')
        else:
            if (n3 >= n1):
                if (n3 >= n2):
                    print('O número',n3,'é o maior')

