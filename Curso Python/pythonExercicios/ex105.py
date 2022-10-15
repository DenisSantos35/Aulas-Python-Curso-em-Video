

def notas(*n, sit = False):
    """
    -> Funcao para anailzar notas e situações de varios alunos.
    :param n:   uma ou mais notas de varios alunos (aceita varias notas)
    :param sit: Valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionario com varias informações sobre situação da turma
    """
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] < 5:
            dados['situação'] = 'RUIM'
        elif 5 < dados['media'] < 7:
            dados['situação'] = 'RAZOAVEL'
        elif dados['media'] > 7:
            dados['situação'] = 'BOA'
    return dados


resp  = notas(3.5, 10, 6.5, sit = True)
print(resp)
help(notas)
