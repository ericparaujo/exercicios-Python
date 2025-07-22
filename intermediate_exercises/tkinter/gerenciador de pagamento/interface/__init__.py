import tkinter


def janela_principal():
    janela = tkinter.Tk()
    janela.geometry('640x480')
    janela.title('GERENCIADOR DE PAGAMENTO')

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_columnconfigure(1, weight=1)

    coluna1 = tkinter.Frame(janela, bg = 'blue')
    coluna2 = tkinter.Frame(janela, bg = 'red')

    coluna1.grid(row=0, column=0, sticky='nesw')
    coluna2.grid(row=0, column=1, sticky='nesw')

    label1 = tkinter.Label(coluna1, text='texto 1')
    label1.pack(pady=40)
    label2 = tkinter.Label(coluna2, text='texto 2' )
    label2.pack(pady=40)

    janela.mainloop()






janela_principal()