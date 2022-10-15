from exteste.lib.criararquivo import *
#Verificação se existe arquivo existente
arquivo = 'teste.txt' #passa nome do arquivo para verificaçao
if criarVerificarArquivo(arquivo):
    print('Arquivo ja existente')
else:
    print('Arquivo não existe: ')
#Criaçao de arquivo
    criarNewArquivo(arquivo)
lerArquivo(arquivo)

