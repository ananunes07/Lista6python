'''
Autor: Ana Clara Nunes
Data: 12/07/2018

Questão 14
'''
x = 5
m18 = 0

for x in range(1,x+2):
    idade = int(input('Digite a idade: '))

    if idade < 18:
        m18 += 1
      




print(m18,'pessoas são menores de idade')
medi = idade + idade / 6
print ('A média de idade é',medi)
