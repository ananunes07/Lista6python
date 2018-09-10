'''
Autor: Ana Clara Nunes
Data: 12/07/2018

Questão 11
'''
nome = input('Digite sue nome: ')
senha = input('Digite sua senha: ')
if nome == senha:
    print('ERRO')
    print('O nome de usuário e senha não podem ser iguais')
    nome = input('Digite sue nome: ')
    senha = input('Digite sua senha: ')
