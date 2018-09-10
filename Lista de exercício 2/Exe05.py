'''
Autor: Ana Clara Nunes
Data: 17/05/2018

Enunciado:

Questão 5
'''

n1 = int(input('Digite um número:' ))
n2 = int(input('Digite outro número:' ))
n3 = int(input('Digite outro número:' ))

if (n1 >= n2):
    if (n1 >= n3):
        if(n2 >= n3):
            print('O número',n1,'é o maior')
            print('O número',n3,'é o menor')

    if (n1 >= n2):
        if (n1 >= n3):
            if(n3 >= n2):
                print('O número',n1,'é o maior')
                print('O número',n2,'é o menor')
                
if(n2 >= n1):
    if(n2 >= n3):
        if(n3 >= n1):
            print('O número',n2,'é o maior')
            print('O número',n1,'é o menor')

    if(n2 >= n1):
        if(n2 >= n3):
            if(n1 >= n3):
                print('O número',n2,'é o maior')
                print('O número',n3,'é o menor')
                
if(n3 >= n1):
    if(n3 >= n2):
        if(n1 <= n2):
            print('O número',n3,'é o maior')
            print('O número',n1,'é o menor')

    if(n3 >= n1):
        if(n3 >= n2):
            if(n1 >= n2):
                print('O número',n3,'é o maior')
                print('O número',n2,'é o menor')























                    
