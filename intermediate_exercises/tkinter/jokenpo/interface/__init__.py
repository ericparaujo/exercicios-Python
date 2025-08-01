import tkinter

def tela_principal():
    janela = tkinter.Tk()

    janela.geometry('800x600')
    janela.title('PEDRA, PAPEL E TESOURA'.center(220))
    janela.resizable(False, False)
    #divisao da parte superior da janela
    container = tkinter.Frame(janela,
                              bg='blue',
                              padx=10,
                              pady=10)
    container.grid(row=0,
                   column=0,
                   sticky='nsew')
    tkinter.Label(container,
                  text='Vamos jogar pedra, papel e tesoura?'.center(100),
                  bg='yellow').grid(row=0,column=0)


    janela.mainloop()


tela_principal()