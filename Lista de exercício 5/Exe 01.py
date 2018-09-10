'''
Autor: Ana Clara Nunes
Data:30/07/2018

Questão 01 
'''

n = int(input('Digite um número entre 0 a 20:'))
if n > 20 or n < 0:
    print('O número digitado deve estar entre 0 a 20')
    n = int(input('Digite um número entre 0 a 20:'))

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print(num[n])
