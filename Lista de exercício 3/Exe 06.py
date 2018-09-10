'''
Autor: Ana Clara Nunes
Data: 04/06/2018

Enunciado

Questão 6
'''

tc = input('Digite apenas um tipo de carne que deseja comprar: ')
if tc != 'cf' and tc != 'al' and tc != 'pi':
    print('Digite cf para Contra-file, al para Alcatra e pi para Picanha')
    tc = input('Digite apenas um tipo de carne que deseja comprar: ')
q = int(input('Digite a quantidade de carne em quilos que deseja comprar: '))
c = input('A compra será feita no cartão Tabaraja: ')
if c != 'sim' and c != 'nao':
    print('Digite sim ou nao')
    c = input('A compra será feita no cartão Tabaraja: ')
    
if tc == 'cf':
    print('Tipo da carne:Contra-File')
    print('Quantidade de carne',q,'quilos')
    if q <= 5:
        pt = 35 * q
        print('O preço total foi:',pt,'reais')
    if q > 5:
        pt = 29 * q
        print('O preço total foi:',pt,'reais')
    vd = (pt * 5) / 100
    vp = pt - vd
    if c == 'sim':
        print('A compra séra feita no cartão Tabajara')
        print('O valor do desconto será:',vd,'reais')
        print('O valor a pagar sera de:',vp,'reais')
    if c == 'nao':
        print('A compra não será feita no cartão Tabaraja')
        print('Não havera desconto')
        print('O valor a pagar sera de:',pt,'reais')

if tc == 'al':
    print('Tipo da carne:Alcatra')
    print('Quantidade de carne',q,'quilos')
    if q <= 5:
        pt = 33 * q
        print('O preço total foi:',pt,'reais')
    if q > 5:
        pt = 27 * q
        print('O preço total foi:',pt,'reais')
    vd = (pt * 5) / 100
    vp = pt - vd
    if c == 'sim':
        print('A compra séra feita no cartão Tabajara')
        print('O valor do desconto será:',vd,'reais')
        print('O valor a pagar sera de:',vp,'reais')
    if c == 'nao':
        print('A compra não será feita no cartão Tabaraja')
        print('Não havera desconto')
        print('O valor a pagar sera de:',pt,'reais')

if tc == 'pi':
    print('Tipo da carne:Picanha')
    print('Quantidade de carne',q,'quilos')
    if q <= 5:
        pt = 60 * q
        print('O preço total foi:',pt,'reais')
    if q > 5:
        pt = 52 * q
        print('O preço total foi:',pt,'reais')
    vd = (pt * 5) / 100
    vp = pt - vd
    if c == 'sim':
        print('A compra séra feita no cartão Tabajara')
        print('O valor do desconto será:',vd,'reais')
        print('O valor a pagar sera de:',vp,'reais')
    if c == 'nao':
        print('A compra não será feita no cartão Tabaraja')
        print('Não havera desconto')
        print('O valor a pagar sera de:',pt,'reais')

    
 
    
    
