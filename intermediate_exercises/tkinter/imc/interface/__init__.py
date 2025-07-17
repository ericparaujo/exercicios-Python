import tkinter
import exercicios2.imc.interface.estilos


def janela_principal():
    fonte = estilos.configurar_fontes()
    texto = estilos.exibir_texto()

    janela = tkinter.Tk()

    janela.title(f'Calculadora IMC')
    janela.geometry('640x480')

    (tkinter.Label(janela,
                   text = texto['titulo'],fg='blue',
                   font=fonte['titulo']).pack(side='top'))

    tkinter.Label(janela,
                  text = texto['peso'],
                  font = fonte['texto']).place(x = 20, y = 120)

    tkinter.Label(janela,
                  text = texto['altura'],
                  font = fonte['texto']).place(x = 20, y = 180)

    peso = tkinter.Entry(janela,
                         font=fonte['dados'], width = 4)
    peso.place(x = 160, y = 120)

    altura = tkinter.Entry(janela,
                           font=fonte['dados'], width = 4)
    altura.place(x = 160, y = 180)



    tkinter.mainloop()


janela_principal()