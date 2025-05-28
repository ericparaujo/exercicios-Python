def notas(*nota, sit=False):
    """calcula nota e verifica situacao do aluno.
    total = quantidade total de notas
    maior = a maior nota do aluno
    menor = a menor nota do aluno
    media = a nota media do aluno ( soma das notas dividido pela quantidade de notas )"""
    r = dict()
    r['total'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    r['media'] = sum(nota) / len(nota)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'boa'
        elif r['media'] >= 5:
            r['situacao'] = 'regular'
        else:
            r['situacao'] = 'ruim'

    media = sum(nota) / len(nota)
    print(media)
    return r


resp = notas(8, 8, 4, 5, 6, sit=True)

print(resp)
help(notas)