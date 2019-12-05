# -*- coding: <encoding name> -*-

import pyautogui as func
import subprocess
from subprocess import run
from datetime import datetime
import clipboard


def erro():
    func.click(665, 412, interval=0.5)

def openApp(app):    
    func.click(114, 746, interval=3) #barra de pesquisa windows
    set_interval(10)
    func.typewrite(app)
    set_interval(10)
    func.hotkey('enter')
    #func.click(158, 212, interval=20) #clicando no objeto de pesquisa
    #func.click(475, 366, clicks=2, interval=5) #abrindo o objeto de pesquisa
    
def receitaBX(cnpj):
    func.click(856, 745, interval=15) #acessando a janela do programa
    func.click(474, 567, interval=2) #click no botão 'buscar certificado'

    pos_x = 496
    pos_y = 242

    func.click(pos_x, pos_y, clicks=2, interval=0.2) #Acessando pasta do certificado

    func.click(pos_x, pos_y, clicks=2, interval=0.2) #Acessando pasta do certificado4112219300013005122019.txt
    func.click(pos_x, pos_y, clicks=3, interval=0.2) #Acessando pasta do certificado
    func.click(936, 543, interval=0.1) #Acessando o certificado

    func.typewrite('contagil123')

    func.click(652, 418) #Dando 'ok' na senha
    func.click(795, 532) #Abrindo opções de perfil  
    func.click(798, 571) #Selecionando Procurador

    func.click(542, 528, clicks=2, interval=0.5) #Abrindo opções
    func.click(535, 563, interval=0.5) #Selecionando CNPJ
    func.click(576, 531, interval=0.2) #Editando
    func.typewrite(cnpj) #Inserindo CNPJ
    func.click(886, 563)#Entrar

def pesquisaArquivos():
    func.click(255, 123, interval=2) #clicando em pesquisar
    func.click(255, 123) #clicando em pesquisar

    func.hotkey('crtl', 'e')
    
    func.click(924, 222, interval=5) #Abrindo opções
    func.click(768, 304, interval=0.5) #Selecionando SPED FISCAL
    func.click(768, 304) #Selecionando SPED FISCAL

    func.click(669, 248, interval=0.5) #Abrindo opções
    func.click(679, 269, interval=1) #Selecionando SPED FISCAL

def preenchendoDados(data_ini, data_fin):
    func.click(800, 380, interval=0.2) #Acessando o campo data de inicio
    func.typewrite(data_ini)
    
    func.click(644, 400, interval=0.1) #Acessando o campo data de fim
    func.typewrite(data_fin)
    
    func.click(773, 594, interval=0.5) #Pesquisar
    erro()
    func.click(773, 594, interval=0.5) #Pesquisar
        
def set_interval(sec):
    for i in range(sec):
        count = 0

def solicitarArquivo():
    func.click(410, 481, clicks=2, interval=5) #Selecioando o primeiro CNPJ
    func.hotkey('ctrl', 'a')
    func.hotkey('ctrl', 'c')
    func.hotkey('ctrl', 'c')

def criandoArquivo(nome_arq):
    func.click(860, 751, interval=2)
    func.click(677, 394, interval=2)

    func.hotkey('ctrl', 'v')
    func.hotkey('ctrl', 's')
    func.click(812, 625, clicks=2, interval=0.2) #Editando o nome do arquivo
    func.hotkey('ctrl', 'a')
    func.typewrite(nome_arq)
    func.click(1206, 694, interval=1)#clicando em salvar
    func.click(677, 394, interval=2)

    func.hotkey('alt', 'f4')

def fechandoJanela():
     func.hotkey('alt', 'f4')
     func.hotkey('enter')
     
def err():
    text = clipboard.paste()
    if text == "":
        func.click(670, 424, interval=0.2)
        print("ERR!!!")
        return True

    return False
    
def principal(nome_arq, cnpj, data_ini, data_fin):
    run('echo off | clip', check=True, shell=True, stdout=subprocess.PIPE)

    openApp('receitanet')
    set_interval(60)

    receitaBX(cnpj)
    set_interval(10)
    pesquisaArquivos()
    preenchendoDados(data_ini, data_fin)
    set_interval(25)
    solicitarArquivo()
    func.hotkey('alt', 'f4')#Fechando o receita

    openApp('Notas')
    criandoArquivo(nome_arq)

def main():        
    for cnpj in archive:        
        nome_arq = cnpj.rstrip('\n') + date_fin + '.txt'
        principal(nome_arq, cnpj, date_ini, date_fin)    
    
archive = open('CNPJ.txt', 'r')
now = datetime.now()
day = now.day

if(day < 10):
    date_ini = '0' + str(day) + str(now.month) + str(now.year-5)
    date_fin = '0' + str(day) + str(now.month) +  str(now.year)
else:
    date_ini = str(day) + str(now.month) + str(now.year-5)
    date_fin = str(day) + str(now.month) +  str(now.year)

main()
        



