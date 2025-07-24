import tkinter
from tkinter.ttk import Combobox
import estilos
from exercicios2.gerenciador_de_pagamento.gerenciador_pagamento import calcular_valor


def janela_principal():
    fonte = estilos.estilos_fontes()
    texto = estilos.exibir_textos()
    janela = tkinter.Tk()

    def calcular_resultado():
        resultado = calcular_valor(entrada_valor, entrada_opcao)
        janela_resultado.config(text=resultado,
                                fg='dark red')

    janela.geometry('660x480')
    janela.resizable(False, False)
    janela.title(f'GERENCIADOR DE PAGAMENTO'.center(200))

    tkinter.Label(janela,
                  text = texto['titulo'],
                  fg = 'dark green',
                  font = fonte['titulo']).pack(pady=40)
    tkinter.Label(janela,
                  text = texto['valor_produto'],
                  font = fonte['texto2']).place(x=20, y=120)
    tkinter.Label(janela,
                  text = texto['forma_pagamento'],
                  font = fonte['texto2']).place(x=20, y=180)

    entrada_valor = (tkinter.Entry(janela,
                  font=fonte['texto1'], width=9))
    entrada_valor.place(x=220, y=120)

    entrada_opcao = (Combobox(janela,
                  values=estilos.forma_pagamento(),
                  font=fonte['texto1']))
    entrada_opcao.place(x=220, y=180, width=420)

    janela_resultado = tkinter.Label(janela,
                                     text='',
                                     font=fonte['resultado'])
    janela_resultado.place(x=220, y=250)


    tkinter.Button(janela,
                   text=texto['botao'],
                   font=fonte['botao'],
                   width=20, height=2,
                   command=calcular_resultado).pack(pady=40, side="bottom", )



    janela.mainloop()




if __name__ == '__main__':
    janela_principal()