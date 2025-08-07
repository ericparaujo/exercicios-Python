import tkinter
from tkinter.ttk import Combobox


def tela_principal():
    janela = tkinter.Tk()

    janela.geometry('800x600')
    janela.title('PEDRA, PAPEL E TESOURA'.center(220))
    janela.resizable(False, False)

    #divisao da parte superior da janela com titulo e subtitulo
    container = tkinter.Frame(janela,
                              bg='blue',
                              padx=10,
                              pady=10)
    container.grid(row=0,
                   column=0,
                   sticky='nsew')
    tkinter.Label(container,
                  text='Vamos jogar pedra, papel e tesoura?'.center(69),
                  font=('times new roman', 24, 'bold'),
                  bg='yellow').grid(row=0,column=0)

    container2 = tkinter.Frame(janela,
                               padx=10,
                               pady=30)
    container2.grid(row=1,
                    column=0,
                    sticky='nsew')
    tkinter.Label(container2,
                  text='escolha uma opção'.center(115),
                  font=('arial', 16, 'bold')).grid(row=0,column=0)

    # botoes de escolha do usuario
    container3 = tkinter.Frame(janela,
                               padx=10,
                               pady=10)
    container3.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    container3.grid(row=2,
                    column=0,
                    sticky='nsew')
    tkinter.Button(container3,
                   text=' Pedra ',
                   font=('arial', 16)).grid(row = 0, column=2)
    tkinter.Button(container3,
                   text=' Papel ',
                   font=('arial', 16)).grid(row=0, column=3)
    tkinter.Button(container3,
                   text='Tesoura',
                   font=('arial', 16)).grid(row=0, column=4)

    # escolha do sistema
    tkinter.Label(container3,
                  text='Eu escolhi:',
                  font=('arial', 16)).grid(row=4, column=3, pady=50)
    tkinter.Label(container3,
                  text='aparece o random aqui',
                  font=('arial', 16)).grid(row=5, column=3)

    container4 = tkinter.Frame(janela,
                               padx=10,
                               pady=10)
    container4.grid(row=3,
                    column=0,
                    sticky='nsew')
    tkinter.Label(container4,
                  text='aparece se ganhou ou perdeu',
                  bg='blue',
                  font=('arial', 16)).grid(padx=250, pady=1, )




    janela.mainloop()


if __name__ == '__main__':
    tela_principal()