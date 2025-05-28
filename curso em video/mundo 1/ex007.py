# media das notas de um aluno
nota1 = float(input('\033[32mdigite uma nota: \033[m'))
nota2 = float(input('\033[32mdigite outra nota: \033[m'))
media = (nota1 + nota2)/2
print('\033[7msuas notas foram: {:.1f} e {:.1f} \nSua media será: {:.1f}\033[m'.format(nota1, nota2, media))
