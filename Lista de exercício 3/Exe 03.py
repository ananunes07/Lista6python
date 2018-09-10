'''
Autor: Ana Clara Nunes
Data: 04/06/2018

Enunciado

Questão 3
'''
s = float(input('Digite o seu salário: '))

a20 = (s * 20) / 100
an20 = s + a20
a15 = (s * 15) / 100
an15 = s + a15
a10 = (s * 10) / 100
an10 = s + 10
a5 = (s * 5) / 100
an5 = s + a5

if s <= 940:
    print('o salário antes do reajuste:',s,)
    print('o percentual de aumento aplicado: 20%')
    print('o valor do aumento:',a20)
    print('o novo salário, após o aumento:',an20,)

if 940 < s <= 1200:
    print('o salário antes do reajuste:',s,)
    print('o percentual de aumento aplicado: 15%')
    print('o valor do aumento:',a15)
    print('o novo salário, após o aumento:',an15,)

if 1200 < s < 1800:
    print('o salário antes do reajuste:',s,)
    print('o percentual de aumento aplicado: 10%')
    print('o valor do aumento:',a10)
    print('o novo salário, após o aumento:',an10,)

if s >= 1800:
    print('o salário antes do reajuste:',s,)
    print('o percentual de aumento aplicado: 5%')
    print('o valor do aumento:',a5)
    print('o novo salário, após o aumento:',an5,)
