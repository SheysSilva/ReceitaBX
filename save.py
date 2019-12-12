# -*- coding: <encoding name> -*-

import pyautogui as func
import subprocess
from subprocess import run
from datetime import datetime
import clipboard
import os

path = 'C:\\Users\\Sheilla.CONTAGIL2\\Documents\\Contagil\\ReceitaBX\\'
path_data = 'src\\data\\'
path_static = 'src\\static\\'

def erro():
    func.click(665, 412, interval=0.5)

#Abre o programa/aplicativo.
#PARAMETRO: name_app (nome do programa/aplicativo).
def openApp(name_app):
    #Clica na barra de pesquisa/icone do sistema.
    func.click(130, 750, interval=3)

    #Escreve o nome do programa/aplicativo.    
    func.typewrite(name_app)

    #Clica em 'enter' para abrir o aplicativo.
    func.hotkey('enter')

    #Caso a função acima não funcione, use uma das opções abaixo:
        #Remova o '#' para descomentar o código.

    #Clica no programa/aplicativo da pesquisa.
    #func.click(158, 212, interval=20)
    
    #Abre o programa/aplicativo da pesquisa.
    #func.click(475, 366, clicks=2, interval=5)

#Salva os dados do arquivo.
def salvandoArquivo(nome_arquivo):
    files = os.listdir(path+path_data)
    if nome_arquivo in files:
        print("Acessando Arquivo: "+ str(nome_arquivo))
        subprocess.Popen(["notepad", path+path_data+nome_arquivo])

        #Acessando a janela do arquivo.
        func.click(860, 751, interval=2)
        func.click(677, 394, interval=2)

        #Colando os dados no arquivo.
        func.hotkey('ctrl', 'end')
        func.hotkey('enter')
        func.hotkey('ctrl', 'v')

        #Abrindo a opção para salvar.
        func.hotkey('ctrl', 's')

        #Acessando a janela do arquivo.
        func.click(855, 751, interval=2)
        func.click(677, 394, interval=2)

        #Fecha o arquivo TXT.
        func.hotkey('alt', 'f4')
        func.hotkey('enter')

    else:
        print("Criando Arquivo: " + str(nome_arquivo))
        openApp('Bloco de Notas')
        criandoArquivo(nome_arquivo)

#Criando arquivo TXT.
def criandoArquivo(nome_arq):
    #Acessando a janela do arquivo.
    func.click(860, 751, interval=2)
    func.click(677, 394, interval=2)

    #Colando os dados no arquivo.
    func.hotkey('ctrl', 'v')

    #Abrindo a opção para salvar.
    func.hotkey('ctrl', 's')

    #Acessando o campo para edição do nome do arquivo.
    func.click(812, 625, clicks=2, interval=0.2)

    #Seleciona tudo que estiver no campo nome.
    func.hotkey('ctrl', 'a')

    #Atualiza o nome do arquivo.
    func.typewrite(nome_arq)

    #Salvando na pasta de Dados do programa.

    #Clica no botão 'salvar'.
    func.click(1206, 694, interval=1)
    func.click(677, 394, interval=2)

    #Acessando a janela do arquivo.
    func.click(860, 751, interval=2)
    func.click(677, 394, interval=2)

    #Fecha o arquivo TXT.
    func.hotkey('alt', 'f4')

def err():
    text = clipboard.paste()
    if text == "":
        func.click(670, 424, interval=0.2)
        print("ERR!!!")
        return True

    return False

def principal(nome_arq, cnpj, data_ini, data_fin):
    run('echo off | clip', check=True, shell=True, stdout=subprocess.PIPE)
    salvandoArquivo(nome_arq)

def main():        
    for cnpj in archive:        
        nome_arq = cnpj.rstrip('\n') + '.txt'
        principal(nome_arq, cnpj, date_ini, date_fin)    
    
archive = open(path+path_static+'CNPJ.txt', 'r')
now = datetime.now()
day = now.day

if(day < 10):
    date_ini = '0' + str(day) + str(now.month) + str(now.year-5)
    date_fin = '0' + str(day) + str(now.month) +  str(now.year)
else:
    date_ini = str(day) + str(now.month) + str(now.year-5)
    date_fin = str(day) + str(now.month) +  str(now.year)

main()
        



