#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import threading
from urllib.request import urlopen
from unicodedata import normalize
from html.parser import HTMLParser
from crawler import EncontraMusica
paginainicial = 'https://www.vagalume.com.br'
listademusica = set()
banda = "semnome"

#escreve num arquivo que tem o nome da banda todas as músicas encontradas
def write_file(listamusica):
    try:
        escrever = open(banda+".txt", mode="w", encoding="utf-8")
        tamanho = len(listamusica)
        x = 0
        if(qtdm == "tudo" or int(qtdm)>tamanho):
            while x < tamanho:
                escrever.write(listamusica[x]+"\n")
                x+=1
        else:
            while x < int(qtdm):
                escrever.write(listamusica[x]+"\n")
                x+=1
        escrever.close()
    except Exception as ex:
        print(ex)
        exit()

#se a entrada for um arquivo ele encontra o nome da banda por aqui
def read_file_ini(nomearquivo):
    try:        
        lera = open(nomearquivo, mode="r", encoding="utf-8")
        nomebanda = lera.read()
        lera.close()
        nomebanda = nomebanda.replace(" ", "-")
        if("&" in nomebanda):
            nomebanda = nomebanda.replace("&-","")
        return nomebanda.lower()
    except:
        print("arquivo não encontrado, encerrando o programa")
        exit()

#se for um arquivo de entrada ele trata para ler o conteúdo do arquivo, se foi só o nome de uma banda ele não precisa ler arquivo
def lerentrada(lista):
    if("." in lista):
        nomebanda = read_file_ini(lista)
    else:
        nomebanda = lista.replace(" ", "-")
        if("&" in nomebanda):
            nomebanda = nomebanda.replace("&-","")
    return normalize('NFKD', nomebanda).encode('ASCII', 'ignore').decode('ASCII').lower()


#faz desda validação da banda até a criação da lista de músicas da banda
def val_banda(banda, qtdm):
    try:
        url = paginainicial+"/"+banda
        response = urlopen(url) #verifica se tem alguma resposta do html
        htmlfonte = response.read() #recebe o html
        htmlfontelegivel = htmlfonte.decode("utf-8") #torna o html legivel
        musicas = EncontraMusica(qtdm) # cria o objeto para analisar o html e encontrar as musicas
        musicas.feed(htmlfontelegivel) # alimenta o objeto com o html, aqui ele já faz toda a analise do html e cria a lista de musicas   
        write_file(musicas.lista_musicas()) #escreve num arquivo a lista de musicas
        musicas.imprime_lista() #imprime no prompt
    except Exception as ex:
        print("Banda não encontrada no vagalume, encerrando o programa")
        exit()

#caso receba parametro na linha de comando, chama o lerentrada
def banda():
    if(len(sys.argv)>1):
        entrada = " ".join(sys.argv[1:len(sys.argv)])
        banda = lerentrada(entrada)
    else:
        name = input("Insira o nome da banda ou o nome do arquivo com a extenção .txt:\n")
        while(not name):
            print("Sem parâmetro não é valido\n")
            name = input("Insira o nome da banda ou o nome do arquivo com a extenção .txt:\n")
        banda = lerentrada(name)
    return banda

#ve a quantidade de músicas que o deseja ser listadas
def qtd():
    try: 
        qtdm = input("Digite a quantidade de músicas que deseja listar, ele precisa ser um número inteiro.\n")
        if(not qtdm):
            print("Não foi definido um valor, então será considerado todas as músicas.")
            qtdm = "tudo"
            return qtdm
        elif (not qtdm.isdigit()):
            print("O valor digitado \""+qtdm+"\" não é valido.\n")
            return qtd()
        else:
            return qtdm

    except Exception as ex:
        pass


banda = banda()
qtdm = qtd()
val_banda(banda, qtdm)

