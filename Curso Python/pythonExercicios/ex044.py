produto = float(input('Digite o valor do produto: '))
print('''Qual vai ser a forma de pagamento?
[1] A vista dinheiro/cheque
[2] A vista no cartao
[3] Parcelado no cartão até 2 Vezes
[4] Parcelado no carto 3 vezes ou mais''')
opcao = int(input('Escolha sua opçao'))
if opcao == 3:
    pagamento = int(input('Vai parcelar em 1 ou 2 vezes?'))
    while((pagamento < 0) or (pagamento >=3 )):
            pagamento = int(input('Vai parcelar em 1 ou 2 vezes?'))
elif opcao == 4:
    pagamento = int(input('Vai parcelar em quantas vezes acima de 3?'))
    while(pagamento < 3 ):
            pagamento = int(input('Vai parcelar em quantas vezes acima de 3?'))
if (opcao == 1):
    desconto = produto - (produto * 0.10)
    print('A vista no dinheiro ou cheque voce terá 10% de desconto\n'
          'o Valor total do seu produto sera de {:.2f} R$'.format(desconto))
elif (opcao == 2):
    desconto = produto - (produto * 0.05)
    print('A vista no cartao voce terá 5% de desconto.\n'
          'o Valor total do seu produto sera de {:.2f} R$'.format(desconto))
elif (opcao == 3):
    produto = produto
    parcela = produto / pagamento
    print('Pagamento no cartao em {} vezes nao havera juros.'.format(pagamento))
    print('o valor do produto sera de{:.2f}'.format(produto))
    print('O valor parcelado sera de{} X {:.2f}R$'.format(pagamento, parcela))
elif (opcao == 4):
    juros = produto + (produto * 0.20)
    parcela = juros / pagamento
    print('Pagamento no cartao em {} vezes tera um juros de 20%,\n'
          'o valor do produto sera de{} R$'.format(pagamento, juros))
    print('O valor parcelado sera de {} X {:.2f}R$'.format(pagamento, parcela))
else:
    print('Opçao invalida, tente novamente')
