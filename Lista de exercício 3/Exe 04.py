'''
Autor: Ana Clara Nunes
Data: 30/05/2018

Enunciado:

Questão 4

'''

valor = int(input('Valor que deseja sacar: '))

nota2 = 0
nota5 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0

if valor < 10 or valor > 800:
    print('Não pode sacar esse valor')
else:
    nota100 = valor // 100
    valor = valor - nota100 * 100
    nota50 = valor // 50
    valor = valor - nota50 * 50
    nota20 = valor // 20
    valor = valor - nota20 * 20
    nota10 = valor // 10
    valor = valor - nota10 * 10
    nota5 = valor // 5
    valor = valor - nota5 * 5
    nota2 = valor // 2
    valor = valor - nota2 * 2

    if valor != 0:
        print('Sugiro o saque de:', nota2*2 +nota5*5 + nota10*10 + nota20*20 + nota50*50 + nota100*100)
    
    if nota2 != 0:
        print(nota2, 'notas de R$ 2,00')
    if nota5 != 0:
        print(nota5, 'notas de R$ 5,00')
    if nota10 != 0:
        print(nota10, 'notas de R$ 10,00')
    if nota20 != 0:
        print(nota20, 'notas de R$ 20,00')
    if nota50 != 0:
        print(nota50, 'notas de R$ 50,00')
    if nota100 != 0:
        print(nota100, 'notas de R$ 100,00')
