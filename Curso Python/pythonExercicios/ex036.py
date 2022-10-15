valor = float(input('Qual o valor do imovel? '))
salario = float(input('Qual o valor do salario?'))
q_anos = int(input('Em quantos anos deseja parcelar?'))

meses = q_anos * 12
prestacao = valor / meses
percentual = salario * 0.30

if prestacao > percentual:
    print('Emprestimo negado, o valor da prestação execeu 30% do salario')
else:
    print('Emprestimo liberado, o valor da parcela e de {:.2f}R$, parcelados em {} meses'.format(prestacao,meses))
