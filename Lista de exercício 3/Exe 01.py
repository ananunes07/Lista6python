'''
Autor: Ana Clara Nunes
Data: 04/06/2018

Enunciado

Questão 1
'''
n = int(input('Digite o número: '))

if n == 1 or n == 8 or n == 15 or n == 22 or n == 29: 
    print('Domingo')
if n == 2 or n == 9 or n == 16 or n == 23 or n == 30:
    print('Segunda feira')
if n == 3 or n == 10 or n == 17 or n == 24 or n == 31:
    print('Terça feira')
if n == 4 or n == 11 or n == 18 or n == 25:
    print('Quarta feira')
if n == 5 or n == 12 or n == 19 or n == 26:
    print('Quinta feira')
if n == 6 or n == 13 or n == 20 or n == 27:
    print('Sexta feira')
if n == 7 or n == 14 or n == 21 or n == 28:
    print('Sábado')
if n > 31:
    print('Valor inválido')
        
