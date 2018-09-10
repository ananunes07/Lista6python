'''

Autor: Ana Clara Nunes
Data: 02/07/2018

Questão 05

'''

i1 = int(input('Digite a idade: '))
i2 = int(input('Digite a idade: '))
i3 = int(input('Digite a idade: '))
i4 = int(input('Digite a idade: '))
i5 = int(input('Digite a idade: '))
i6 = int(input('Digite a idade: '))
i7 = int(input('Digite a idade: '))
i8 = int(input('Digite a idade: '))
i9 = int(input('Digite a idade: '))
i10 = int(input('Digite a idade: '))

ida_inf = 0
ida_med = (i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10) / 10


if i1 < 30:
    ida_inf = ida_inf + 1
if i2 < 30:
    ida_inf = ida_inf + 1
if i3 < 30:
    ida_inf = ida_inf + 1
if i4 < 30:
    ida_inf = ida_inf + 1
if i5 < 30:
    ida_inf = ida_inf + 1
if i6 < 30:
    ida_inf = ida_inf + 1
if i7 < 30:
    ida_inf = ida_inf + 1
if i8 < 30:
    ida_inf = ida_inf + 1
if i9 < 30:
    ida_inf = ida_inf + 1
if i10 < 30:
    ida_inf = ida_inf + 1

print('O número de membros que tem idade inferior a 30 anos é igual a:', ida_inf)
print('A idade média dos membros é:',ida_med)   


