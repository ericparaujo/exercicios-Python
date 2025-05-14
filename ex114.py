import urllib
import urllib.request

pudim = 'https://www.pudim.com.br'

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')

except urllib.error.URLError:
    print('endereco invalido')
else:
    print('conteudo acessivel')
    print(site.read())
