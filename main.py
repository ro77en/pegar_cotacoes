import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfile
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dict_moedas = requisicao.json()

lista_moedas = list(dict_moedas.keys())


def pegar_cotacao():
    moeda = combobox_selec_moeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = float(cotacao[0]['bid'])
    label_cotacao_output['text'] = f"Cotação de {moeda} no dia {data_cotacao}: R$ {valor_moeda:,.2f}"

def selecionar_arquivo():
    caminho_arquivo = askopenfile(title='Selecione o Arquivo de Moeda')
    var_caminho_arquivo.set(caminho_arquivo)
    if caminho_arquivo:
        pass

def atualizar_cotacoes():
    pass

janela = tk.Tk()
janela.title('Cotação de Moedas')

# cotação de uma moeda

title1 = tk.Label(text='Cotação de 1 Moeda Específica', borderwidth=2, relief='solid', fg='white', bg='black')
title1.grid(row=0, column=0, pady=10, sticky='nswe', columnspan=3)

label_selec_moeda = tk.Label(text='Selecione a Moeda Desejada: ', anchor='e')
label_selec_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

combobox_selec_moeda = ttk.Combobox(values=lista_moedas)
combobox_selec_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nsew')

label_selec_dia = tk.Label(text='Selecione o dia que deseja pegar a cotação: ', anchor='e')
label_selec_dia.grid(row=2, column=0, padx=10, pady=10, sticky='nsew', columnspan=2)

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_cotacao_output = tk.Label(text='')
label_cotacao_output.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

btn_pegar_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
btn_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')

# cotação de várias moedas

title2 = tk.Label(text='Cotação de Múltiplas Moedas', borderwidth=2, relief='solid', fg='white', bg='black')
title2.grid(row=4, column=0, pady=10, sticky='nswe', columnspan=3)

label_selec_arquivo = tk.Label(text='Selecione um arquivo Excel com as Moedas na Coluna A...', anchor='e')
label_selec_arquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

var_caminho_arquivo = tk.StringVar()

btn_selec_arquivo = tk.Button(text='Selecionar Arquivo', command=selecionar_arquivo)
btn_selec_arquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')

label_arquivo_selec = tk.Label(text='Nenhum Arquivo Selecionado', anchor='e')
label_arquivo_selec.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

label_data_ini = tk.Label(text='Data Inicial', anchor='e')
label_data_fin = tk.Label(text='Data Final', anchor='e')
label_data_ini.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
label_data_fin.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')

calendario_data_ini = DateEntry(year=2023, locale='pt_br')
calendario_data_fin = DateEntry(year=2023, locale='pt_br')
calendario_data_ini.grid(row=7, column=1, padx=10, pady=10, sticky='nsew')
calendario_data_fin.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')

btn_atualizar_cotacoes = tk.Button(text='Atualizar Cotações', command=atualizar_cotacoes)
btn_atualizar_cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')

label_atualizar_cotacoes = tk.Label(text='')
label_atualizar_cotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

btn_fechar = tk.Button(text='Fechar', command=janela.quit)
btn_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')

janela.mainloop()