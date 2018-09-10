'''
Autor: Ana Clara Nunes
Data: 14/05/2018

Enunciado:

Faça um programa que peça os três lados de um triângulo. O programa deverá informar se os valores poem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

'''

A = float(input('Digite o lado A: '))
B = float(input('Digite o lado B: '))
C = float(input('Digite o lado C: '))

if (B - C) < A < B + C or (A - C) < B < A + C or (A - B) < C < A + B:
    if A == B == C:
        print('É um triângulo equilátero')

if (B - C) < A < B + C or (A - C) < B < A + C or (A - B) < C < A + B:
    if A == C or A == B or B == C:
        print('É um triângulo isósceles')
   
if (B - C) < A < B + C or (A - C) < B < A + C or (A - B) < C < A + B:
    if A != B != C:
        print('É um triângulo escaleno')
else:
    print ('Não é um triângulo')
        
 
    
   
