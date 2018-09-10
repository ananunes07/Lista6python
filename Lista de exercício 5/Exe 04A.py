'''
Autor: Ana Clara Nunes
Data:01/08/2018

Questão 04
'''
p = 0
 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

tu = (n1,n2,n3,n4)

print ('O valor 9 aparece',tu.count(9),'veze(s)')

if tu.index(3):
    print ('O valor 3 foi digitado na posição número',tu.index(3))
else:
    print ('O número 3 não foi digitado')

if int(n1) % 2 == 0:
    print ('O número',n1,'é par')
else:
    print ('O número',n1,'é impar')
    
if int(n2) % 2 == 0:
    print ('O número',n2,'é par')
else:
    print ('O número',n2,'é impar')

if int(n3) % 2 == 0:
    print ('O número',n3,'é par')
else:
    print ('O número',n3,'é impar')

if int(n4) % 2 == 0:
    print ('O número',n4,'é par')
else:
    print ('O número',n4,'é impar')

    



