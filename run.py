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

#Loga no programa da ReceitaBX.
def loginReceitaBX(cnpj):
    #Acessa a janela do programa.
    func.click(856, 745, interval=15)
    
    #Clica no botão 'buscar certificado'.
    func.click(474, 567, interval=2) 

    #Posição da pasta do topo dos caminhos percorridos.
    #Acessa a primeira pasta ou arquivo do topo.
    pos_x = 496
    pos_y = 242

    #Acessando as pastas do certificado.
    func.click(pos_x, pos_y, clicks=2, interval=0.2) 
    func.click(pos_x, pos_y, clicks=2, interval=0.2)
    func.click(pos_x, pos_y, clicks=3, interval=0.2)

    #Selecionando o certificado.
    func.click(936, 543, interval=0.1) 

    #Inserindo a senha do certificado.
    func.typewrite('contagil123')

    #Clicando no botão 'ok'.
    func.click(652, 418)

    #Abrindo opções de perfil  de acesso.
    func.click(795, 532)

    #Selecionando a opção: Procurador.
    func.click(798, 571) 

    #Abrindo as opções de representação.
    func.click(542, 528, clicks=2, interval=0.5)

    #Selecionando a opção: CNPJ.
    #func.click(535, 563, interval=0.5)
    func.hotkey('down')

    #Clicando no campo para inserir o CNPJ.
    func.click(576, 531, interval=0.2)

    #Inserindo o CNPJ.
    func.typewrite(cnpj)

    #Clicando no botão 'entrar'.
    func.click(886, 563)

#Acessando a janela de pesquisa de arquivos.
def pesquisaArquivos():
    #Clicando na opção de Pesquisar.
    func.click(255, 123, interval=2) 

    #Comando para ir para a janela de Pesquisar.
    func.hotkey('crtl', 'e')

    #Abrindo opções de sistema.
    func.click(924, 222, interval=5)

    #Selecionando a opção: SPED FISCAL.
    func.click(768, 304, interval=0.5)

    #Abrindo opções de tipo de arquivo.
    func.click(669, 248, interval=0.5)

    #Selecionando a opção: Escrituração Fiscal Digital.
    func.click(679, 269, interval=1) 

#Preenchando os dados pata a pesquisa.
def preenchendoDados(data_ini, data_fin):
    #Acessando o campo data de inicio.
    func.click(800, 380, interval=0.2)

    #Inserindo a data de inicio.
    func.typewrite(data_ini)

    #Acessando o campo data final.
    func.click(644, 400, interval=0.1)

    #Inserindo a data final.
    func.typewrite(data_fin)

    #Cliando no botão 'pesquisar'.
    func.click(773, 594, interval=0.5)

    #Ajustando para a caixa de alerta.
    erro()
    func.click(773, 594, interval=0.5) 

#Selecionando os arquivos para copiar.
def solicitarArquivo():
    #Selecioando o primeiro CNPJ
    func.click(410, 481, clicks=2, interval=5)

    #Selecioando os outros cnpjs.
    func.hotkey('ctrl', 'a')

    #Copiando todos os cnpjs.
    func.hotkey('ctrl', 'c')
    func.hotkey('ctrl', 'c')


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
    openApp('receitanet')

    loginReceitaBX(cnpj)
    pesquisaArquivos()
    preenchendoDados(data_ini, data_fin)
    solicitarArquivo()
    
    #Fecha o programa da ReceitaBX.
    func.hotkey('alt', 'f4')

def main():        
    for cnpj in archive:        
        nome_arq = cnpj.rstrip('\n') + date_fin + '.txt'
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
        



