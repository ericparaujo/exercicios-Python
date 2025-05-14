from datetime import date
atual = date.today().year
maior = 0
menor = 0

for pess in range(1, 8):
      nascimento = int(input(f'digite o {pess}° ano de nascimento: '))
      idade = atual - nascimento
      if idade >= 21:
          maior += 1
      else:
          menor += 1

print(f'ao todos tivemos {maior} maiores de 21 anos')
print(f'e tivemos {menor} menores de 21 anos')