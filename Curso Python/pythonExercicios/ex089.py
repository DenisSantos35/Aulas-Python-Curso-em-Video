aluno = list()
notas = list()
boletim = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    aluno.append(nome)
    aluno.append(n1)
    notas.append(n1)
    aluno.append(n2)
    notas.append(n2)
    aluno.insert(0,notas[:])
    aluno.append(media)
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print('-='*60)
print('{:<3} {:<17} {}'.format('Nº', 'NOME', 'MÉDIA'))
print('-'*60)
cont = 0
for n, status in enumerate(boletim):
    print('{:<4}'.format(n), end='')
    print('{:<20}'.format(boletim[n][1]), end='')
    print('{}'.format(boletim[n][4]))
print('-'*60)
while True:
    msg = int(input('Mostrar notas de qual aluno? [999] interrompe: '))
    print('-'*60)
    if msg == 999:
        break
    for pos, mostrar in enumerate(boletim):
        if pos == msg:
            print('Notas de {} são {}'.format(boletim[pos][1],boletim[pos][0]))
            print('-'*60)





