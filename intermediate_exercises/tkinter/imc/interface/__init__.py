import tkinter
import exercicios2.imc.interface.estilos
from exercicios2.imc.imc import condicionais

"""
MODULO FONT-END
"""

def janela_principal():
    fonte = estilos.configurar_fontes()
    texto = estilos.exibir_texto()

    janela = tkinter.Tk()

    janela.title(f'Calculadora IMC')
    janela.geometry('640x480')

    (tkinter.Label(janela,
                   text = texto['titulo'],fg = 'blue',
                   font = fonte['titulo']).pack(side = 'top'))

    tkinter.Label(janela,
                  text = texto['peso'],
                  font = fonte['texto']).place(x = 20, y = 120)

    tkinter.Label(janela,
                  text = texto['altura'],
                  font = fonte['texto']).place(x = 20, y = 180)

    peso_entrada = tkinter.Entry(janela,
                         font=fonte['dados'], width = 4)
    peso_entrada.place(x = 160, y = 120)

    altura_entrada = tkinter.Entry(janela,
                           font=fonte['dados'], width = 4)
    altura_entrada.place(x = 160, y = 180)

    resultado_titulo = tkinter.Label(janela,
                                     text = '',
                                     font = fonte['dados'])
    resultado_titulo.place(x = 160, y = 300)

    def calcular():
        resultado = condicionais(peso_entrada, altura_entrada)
        resultado_titulo.config(text = resultado)


    botao = tkinter.Button(janela,
                           text = 'calcular',
                           font = fonte['dados'],
                           command=calcular)
    botao.place(x = 160, y = 400)


    tkinter.mainloop()



