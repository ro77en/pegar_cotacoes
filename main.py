import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']

def pegar_cotacao():
    pass

janela = tk.Tk()
janela.title('Cotação de Moedas')

title1 = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid')
title1.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selec_moeda = tk.Label(text='Selecione a Moeda Desejada: ')
label_selec_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

combobox_selec_moeda = ttk.Combobox(values=lista_moedas)
combobox_selec_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selec_moeda = tk.Label(text='Selecione o dia que deseja pegar a cotação: ')
label_selec_moeda.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_cotacao_output = tk.Label(text='')
label_cotacao_output.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

btn_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
btn_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

title2 = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid')
title2.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)


janela.mainloop()