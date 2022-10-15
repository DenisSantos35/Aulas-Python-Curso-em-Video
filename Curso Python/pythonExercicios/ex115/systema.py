from ex115.lib.interface import * #importacao do caminho a ser percorrido diretorio ex115, lib, interface
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExiste(arq):
      criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # opcao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opcao para cadastrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida.\033[m')
    sleep(1)
