from lib.interface import *
from lib.arquivo import *

arq = 'arqprojeto.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

lista = ['Ver Pessoas Cadastradas', 'Cadastrar Pessoa', 'Sair do Sistema']
while True:
    resp = menu(lista)
    if resp == 1:
        #Listar conteudo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        #Cdastrar uma nova pessoa
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        #Sair do sistema
        print('Saindo do Sistema... \nAté Logo!')
        break
    else:
        #Digito invalido
        print('\033[31mERRO! Digite uma opção válida!\033[m')

