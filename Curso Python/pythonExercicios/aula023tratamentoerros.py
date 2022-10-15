try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print(f'Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print(f'O usuario preferiu não informar os dados!')

else:
    print(f'O resultado{r}')
finally:
    print(f'Volte Sempre! Muito obrigado...')

'''except Exception as erro:
   print(f'O problema foi {erro.__class__}')'''
