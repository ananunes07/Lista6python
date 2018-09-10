'''

Autor: Ana Clara Nunes
Data: 02/07/2018

Questão 07

'''

n1 = int(input('Digite o número: '))
n2 = int(input('Digite o número: '))
n3 = int(input('Digite o número: '))
n4 = int(input('Digite o número: '))
n5 = int(input('Digite o número: '))
n6 = int(input('Digite o número: '))
n7 = int(input('Digite o número: '))
n8 = int(input('Digite o número: '))
n9 = int(input('Digite o número: '))
n10 = int(input('Digite o número: '))

n_pos = 0
n_neg = 0
n_nul = 0
m_ari = 0
So_n_pos = 0
q = 0

if n1 > 0:
    n_pos = n_pos + 1
if n2 > 0:
    n_pos = n_pos + 1
if n3 > 0:
    n_pos = n_pos + 1
if n4 > 0:
    n_pos = n_pos + 1
if n5 > 0:
    n_pos = n_pos + 1
if n6 > 0:
    n_pos = n_pos + 1
if n7 > 0:
    n_pos = n_pos + 1
if n8 > 0:
    n_pos = n_pos + 1
if n9 > 0:
    n_pos = n_pos + 1
if n10 > 0:
    n_pos = n_pos + 1



if n1 < 0:
    n_neg = n_neg + 1
if n2 < 0:
    n_neg = n_neg + 1
if n3 < 0:
    n_neg = n_neg + 1
if n4 < 0:
    n_neg = n_neg + 1
if n5 < 0:
    n_neg = n_neg + 1
if n6 < 0:
    n_neg = n_neg + 1
if n7 < 0:
    n_neg = n_neg + 1
if n8 < 0:
    n_neg = n_neg + 1
if n9 < 0:
    n_neg = n_neg + 1
if n10 < 0:
    n_neg = n_neg + 1



if n1 == 0:
    n_nul = n_nul + 1
if n2 == 0:
    n_nul = n_nul + 1
if n3 == 0:
    n_nul = n_nul + 1
if n4 == 0:
    n_nul = n_nul + 1
if n5 == 0:
    n_nul = n_nul + 1
if n6 == 0:
    n_nul = n_nul + 1
if n7 == 0:
    n_nul = n_nul + 1
if n8 == 0:
    n_nul = n_nul + 1
if n9 == 0:
    n_nul = n_nul + 1
if n10 == 0:
    n_nul = n_nul + 1


if n1 > 0:
    So_n_pos = n1
    So_n_pos = So_n_pos
if n2 > 0:
    So_n_pos = n2 + So_n_pos
    So_n_pos = So_n_pos
if n3 > 0:
    So_n_pos = n3 + So_n_pos
    So_n_pos = So_n_pos
if n4 > 0:
    So_n_pos = n4 + So_n_pos
    So_n_pos = So_n_pos
if n5 > 0:
    So_n_pos = n5 + So_n_pos
    So_n_pos = So_n_pos
if n6 > 0:
    So_n_pos = n6 + So_n_pos
    So_n_pos = So_n_pos
if n7 > 0:
    So_n_pos = n7 + So_n_pos
    So_n_pos = So_n_pos
if n8 > 0:
    So_n_pos = n8 + So_n_pos
    So_n_pos = So_n_pos
if n9 > 0:
    So_n_pos = n9 + So_n_pos
    So_n_pos = So_n_pos
if n10 > 0:
    So_n_pos = n10 + So_n_pos
    So_n_pos = So_n_pos

if n1 < 0:
    q = q + 1
    m_ari = m_ari + n1
if n2 < 0:
    q = q +1
    m_ari = m_ari + n2
if n3 < 0:
    q = q + 1
    m_ari = m_ari + n3
if n4 < 0:
    q = q +1
    m_ari = m_ari + n4
if n5 < 0:
    q = q + 1
    m_ari = m_ari + n5
if n6 < 0:
    q = q +1
    m_ari = m_ari + n6
if n7 < 0:
    q = q + 1
    m_ari = m_ari + n7
if n8 < 0:
    q = q +1
    m_ari = m_ari + n8
if n9 < 0:
    q = q + 1
    m_ari = m_ari + n9
if n10 < 0:
    q = q +1
    m_ari = m_ari + n10

m_ari_fin = m_ari / q

print('Existem',n_pos,'número(s) positivos')
print('Existem',n_neg,'número(s) negativos')
print('Existem',n_nul,'número(s) nulos')
print('A média aritmética dos números',m_ari_fin)
print('A soma dos números positivos é',So_n_pos)
