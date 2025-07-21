"""
Modulo destinado a parte grafica.

Nescessita do modulo estilos.py para  funcionar corretamente.

Responsável por montar e exibir a interface gráfica da calculadora de IMC!

Aqui é onde tudo acontece visualmente:
- A janela é criada.
- Campos de entrada são exibidos.
- Botão de 'Calcular' é criado e quando clicado... BAM! Ele mostra o resultado.

Esse é o coração visual do programa
"""

import tkinter
import exercicios2.imc.interface.estilos
from exercicios2.imc.imc import condicionais


def janela_principal():
    fonte = estilos.configurar_fontes()
    texto = estilos.exibir_texto()

    janela = tkinter.Tk()

    janela.title(f'Calculadora IMC')
    janela.geometry('640x480')

    tkinter.Label(janela,
                   text = texto['titulo'],fg = 'blue',
                   font = fonte['titulo']).pack(side = 'top')

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


    tkinter.Label(janela,
                  text = texto['resultado'],
                  font = fonte['titulo']).place(x = 20, y = 250)


    resultado_titulo = tkinter.Label(janela,
                                     text = '',
                                     font = fonte['resultado'])
    resultado_titulo.place(x = 160, y = 300)

    def calcular():
        resultado = condicionais(peso_entrada, altura_entrada)
        resultado_titulo.config(text = resultado,
                                fg='red')


    botao = tkinter.Button(janela,
                           text = 'calcular',
                           font = fonte['dados'],
                           command = calcular)
    botao.place(x = 260, y = 400)


    tkinter.mainloop()



