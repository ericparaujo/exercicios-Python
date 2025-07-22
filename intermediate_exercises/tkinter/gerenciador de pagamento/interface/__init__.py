import tkinter


def janela_principal():
    janela = tkinter.Tk()
    janela.geometry('800x600')
    janela.title(f'GERENCIADOR DE PAGAMENTO'.center(200))

    tkinter.Label(janela,
                  text = exibir_textos()['titulo'],
                  fg = 'green',
                  font = estilos_fontes()['titulo']).pack(pady=40)



    janela.mainloop()


def estilos_fontes():
    return {
        'titulo':('arial', 18, 'bold'),
        'texto1':('arial', 12, 'bold'),
        'texto2':('arial', 12),
        'botao':('arial', 14, 'bold')
    }


def exibir_textos():
    return{
        'titulo':'Gerenciador de pagamento'.center(50).upper()
    }

if __name__ == '__main__':
    janela_principal()