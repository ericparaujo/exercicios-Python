import tkinter
from tkinter.ttk import Combobox
import estilos



def janela_principal():
    fonte = estilos.estilos_fontes()
    texto = estilos.exibir_textos()
    janela = tkinter.Tk()

    janela.geometry('800x600')
    janela.resizable(False, False)
    janela.title(f'GERENCIADOR DE PAGAMENTO'.center(200))

    tkinter.Label(janela,
                  text = texto['titulo'],
                  fg = 'green',
                  font = fonte['titulo']).pack(pady=40)
    tkinter.Label(janela,
                  text = texto['valor_produto'],
                  font = fonte['texto2']).place(x=20, y=120)
    tkinter.Label(janela,
                  text = texto['forma_pagamento'],
                  font = fonte['texto2']).place(x=20, y=180)

    tkinter.Entry(janela,
                  font=fonte['texto1'], width=9).place(x=220, y=120)
    Combobox(janela,
             values=['pagamento a vista no dinheiro',
                     'pagamento a vista no cartao',
                     'pagamento parcelado no cartao [2x]',
                     'Pagamento parcelado no cartao [+ vezes]'],
             font=fonte['texto1']).place(x=220, y=180, width=420)

    tkinter.Button(janela,
                   text=texto['botao'],
                   font=fonte['botao'],
                   width=20, height=2,
                   command='').pack(pady=40, side="bottom", )



    janela.mainloop()




if __name__ == '__main__':
    janela_principal()