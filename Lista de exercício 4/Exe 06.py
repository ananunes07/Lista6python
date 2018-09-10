'''
Autor: Ana Clara Nunes
Data: 04/07/2018

Questão 06

'''

n = 0

mai_alt = 0
mai_alt_nome = ''

q_mul = 0
soma_alt_mul = 0
med_alt_mul = 0

q_hom = 0

while n < 10:

    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ')
    if sexo!= 'M' and sexo != 'F':
        sexo = input('Digite para sexo Masculino M e para Feminino F:')
    altura = float(input('Digite sua altura: '))
    print('----------------------------')

    if altura > mai_alt:
        mai_alt = altura
        mai_alt_nome = nome

    if sexo == 'F':
        q_mul = q_mul + 1
        soma_alt_mul = soma_alt_mul + altura

    else:
        q_hom += 1
    
    n = n + 1

print('{} tem {} e é a maior altura'.format(mai_alt_nome,mai_alt))

med_alt_mul = soma_alt_mul / q_mul
print('A média de altura das mulheres é:',med_alt_mul)

print('A quantidade de Homens é {}'.format (q_hom))

por_mul = q_mul * 100 / (q_mul + q_hom)
print('A porcentagem de mulheres é {}'.format(por_mul))
