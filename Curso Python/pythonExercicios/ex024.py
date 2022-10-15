cidade = str(input('Em que cidade voce nasceu: ')).strip()
resp = 'SANTO' in cidade[:5].upper()
print(resp)
# maneira 2
print(cidade[:5].upper() == 'SANTO')
