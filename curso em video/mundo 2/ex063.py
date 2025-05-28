termo = int(input('digite o primeiro termo: ')) - 2
fibo1 = 0
fibo2 = 1
fibo3 = fibo1 + fibo2
print(f'{fibo1} --> {fibo2} --> ',end='')

while termo != 0:
   print(f'{fibo3} -->',end='')

   fibo1 = fibo2
   fibo2 = fibo3
   fibo3 = fibo1 + fibo2
   termo -= 1
print ('fim')
