
def voto(valor):
    from datetime import date
    ano = date.today().year
    ida = ano - valor
    if ida < 16:
        msg = f'Com {ida} anos: NÃO VOTA '
        return msg
    elif 16 < ida < 18:
        msg = f'Com {ida} anos: VOTO OPCIONAL '
    elif 18 <= ida < 65:
        msg = f'Com {ida} anos: VOTO OBRIGATÓRIO '
        return msg
    else:
        msg = f'Com {ida} anos: VOTO OPCIONAL'
        return msg


#programa principal
idade = int(input('Em que ano voce nasceu? '))
val = voto(idade)
print(val)

