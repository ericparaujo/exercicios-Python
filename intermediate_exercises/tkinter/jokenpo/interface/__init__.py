import tkinter

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



    janela.mainloop()


if __name__ == '__main__':
    tela_principal()