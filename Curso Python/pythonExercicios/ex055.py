maior = 0
menor = 0
pessoa = 0
pes = 0
for i in range(1,6):
    peso = float(input('Digite seu peso: '))
    print('Pessoa n {}, peso:{} Kg'.format(i,peso))
    if(maior < peso):
        maior = peso
        pessoa = i
    if(i == 1):
        menor = peso
    if(menor > peso):
        menor = peso
        pes = i
print('A pessoa numero {}, tem maior peso, pesando: {} Kg'.format(pessoa, maior))
print('A pessoa numero {}, tem menor peso, pesando: {} Kg'.format(pes, menor))
