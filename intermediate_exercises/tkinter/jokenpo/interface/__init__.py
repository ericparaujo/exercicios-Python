import tkinter
from tkinter import Tk

#from exercicios2.jokenpo.jokenpo import minha_escolha


def painel_principal():
    janela = Tk()

    janela.geometry('800x600')
    janela.resizable(False, False)
    janela.title(' PEDRA, PAPEL, TESOURA'.center(180))

    container1 = tkinter.Frame(janela, padx=10, pady=10)
    container1.grid(row=0, column=0, sticky='nsew')
    container2 = tkinter.Frame(janela, pady=10, padx=10)
    container2.grid(row=1, column=0, sticky='nsew')


    tkinter.Label(container1,
                    text='escolha uma opcao:'.center(50),
                    font= ('arial', 18)).grid(row=0, column=0)
    tkinter.Button(container2,
                   text='pedra',
                   font= ('arial', 16),
                   command=lambda: escolha('pedra')).grid(row=0, column=0)
    tkinter.Button(container2,
                   text='papel',
                   font=('arial', 16),
                   command=lambda: escolha('papel')).grid(row=0, column=1)
    tkinter.Button(container2,
                   text='tesoura',
                   font=('arial', 16),
                   command=lambda: escolha('tesoura')).grid(row=0, column=2)



    janela.mainloop()



def escolha(texto=None):
    minha_escolha = texto

    print(texto)
    return minha_escolha



if __name__ == '__main__':
    painel_principal()