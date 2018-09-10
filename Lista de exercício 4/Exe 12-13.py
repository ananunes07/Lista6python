'''
Autor: Ana Clara Nunes
Data: 12/07/2018

Questão 12 e 13
'''
x = 1

print('1. Somar')
print('2. Subtrair')
print('3. Dividir')
print('4. Multiplicar')
print('5. Sair')

op = int(input('Escolha uma opção do menu: '))

while x != 0:
    if op == 1:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        re = n1 + n2
        print('O resultado da operação é:',re)
        print('1. Somar')
        print('2. Subtrair')
        print('3. Dividir')
        print('4. Multiplicar')
        print('5. Sair')
        op = int(input('Escolha uma opção do menu: '))

    if op == 2:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        re = n1 - n2
        print('O resultado da operação é:',re)
        print('1. Somar')
        print('2. Subtrair')
        print('3. Dividir')
        print('4. Multiplicar')
        print('5. Sair')
        op = int(input('Escolha uma opção do menu: '))

    if op == 3:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        re = n1 / n2
        print('O resultado da operação é:',re)
        print('1. Somar')
        print('2. Subtrair')
        print('3. Dividir')
        print('4. Multiplicar')
        print('5. Sair')
        op = int(input('Escolha uma opção do menu: '))

    if op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        re = n1 * n2
        print('O resultado da operação é:',re)
        print('1. Somar')
        print('2. Subtrair')
        print('3. Dividir')
        print('4. Multiplicar')
        print('5. Sair')
        op = int(input('Escolha uma opção do menu: '))

    if op == 5:
        print('SAIR!')
        break

   
