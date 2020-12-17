import os
import PySimpleGUI as sg
from faker import Faker


sg.theme('dark')
#layaute da aplicação
lay = [
    [sg.Button('Gerar Nome ', size = (20, 0)), sg.Input(key = 'nome', size = (60, 0))],
    [sg.Button('Gerar Profissão ', size=(20, 0)), sg.Input(key = 'profissao', size=(60, 0))],
    [sg.Button('Gerar Endereço ', size=(20, 0)), sg.Input(key = 'endereco', size=(60, 0))],
    [sg.Button('Gerar Placa ', size=(20, 0)), sg.Input(key = 'placa', size=(60, 0))],
    [sg.Button('Gerar Cartão de Crédito ', size=(20, 0)), sg.Input(key = 'cartao_credito', size=(60, 0))],
    [sg.Output(size=(85, 15))],
    [sg.Button('Imprimir Pérfil Completo'), sg.Button('Salva Perfil em Arquivo')],
]
#Criando a janela, usando o layaute definido
janela = sg.Window('Faker - Gerador de DADOS Para Teste', layout=lay)
#gerando os dados fake e lendo os arquivos da tela
fake = Faker('pt_BR')
Faker.seed(0)

while 1:
    evento, valores = janela.Read()

    if (evento == sg.WIN_CLOSED):
        break
    elif (evento == 'Gerar Nome '):
        janela['nome'].update('\t' + fake.name())
    elif (evento == 'Gerar Profissão '):
        janela['profissao'].update('\t' + fake.job())
    elif (evento == 'Gerar Endereço '):
        janela['endereco'].update('\t' + fake.address())
    elif (evento == 'Gerar Placa '):
        janela['placa'].update('\t' + fake.license_plate())
    elif (evento == 'Gerar Cartão de Crédito '):
        janela['cartao_credito'].update('  '+fake.credit_card_full())
    elif (evento == 'Imprimir Pérfil Completo'):
        print(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CRÉDITO: {fake.credit_card_full()}{os.linesep}')
    elif (evento == 'Salva Perfil em Arquivo'):
        with open('arquivo_de_teste.txt', 'a', encoding='utf-8', newline='') as arq:
            arq.write(
                f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO DE CRÉDITO: {fake.credit_card_full()}{os.linesep}'
            )
