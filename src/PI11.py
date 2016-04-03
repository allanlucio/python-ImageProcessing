# coding=utf-8
from utils import imgReadAndCopy, mostraImagem
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np



imgCopia,imgOriginal=imgReadAndCopy("../Imagens/Fig0316(3)(third_from_top).tif")


#função que recebe um tamanho e cria uma matriz tamanho*256 que servirá de base para a plotagem do histograma
def criaImagemPreta(tamanho):
    lista=[]
    for linha in range(tamanho):
        lista.append([255]*256)
    return lista

#Essa função recebe uma imagem e conta quantos pixels de cada cor ela tem
#O retorno são 2 dicionário, 1- com a contagem real, 2- com a contagem aplicado a probabilidade, ou seja, normalizado entre 0 e 1.
def contagemDePixels(imagem):
    dist_prob={}
    for i,linha in enumerate(imgCopia):
        for j,col in enumerate(linha):

            try:

                dist_prob[col]+=1
            except:
                dist_prob[col]=1
    total=float(sum(dist_prob.values()))

    probOriginal={}
    for i,valor in enumerate(dist_prob.keys()):

        probOriginal[valor]=dist_prob[valor]/total
    return dist_prob, probOriginal


#Divide o dicionario em intervalos para melhor representar o histograma
#Recebe um dicionario com distribuição de probabilidades e o tamanho do intervalo
def divideEmIntervalos(kwargs,quantidade):
    temp={}
    for a in kwargs.keys():
        indice = a/quantidade
        try:

            temp[indice]+=kwargs[a]

        except:

            temp[indice]=kwargs.get(a)

    return temp

def imprimirProbabilidades(contagem,probabilidade):
    for cont,prob in zip(contagem.keys(),probabilidade.keys()):
        print "Pixel %s - Quantidade: %s  -  Probabilidade: %s%s"%(cont,contagem[cont],(probabilidade[prob]*100),"%")

def getHistogram(imagem,intervalos):


    dist_prob,probOriginal=contagemDePixels(imagem)


    qtd_camadas=256/intervalos #calculando o tamanho do intervalo
    print(qtd_camadas)
    disProb_interval=divideEmIntervalos(dist_prob,qtd_camadas)

    total_newprob=divideEmIntervalos(probOriginal,qtd_camadas)





    print ("Bem vindo, clique qualquer tecla para prosseguir!")
    p=raw_input()
    raw_input("Clique para visualizar a distribuição de probabilidade para toda a imagem\n\n")
    imprimirProbabilidades(dist_prob,probOriginal)
    raw_input("Clique para visualizar a distribuição de probabilidade com intervalos\n\n")
    imprimirProbabilidades(disProb_interval,total_newprob)

    base=510 #valor base que ajusta o histograma, tem que ser multiplo de 255

    tamanhoimg=int(max(total_newprob.values())*(base+20)) #calculo para definir o tamanho da imagem, pra que ela não borre.
    lista=criaImagemPreta(tamanhoimg)

    for key in total_newprob.keys():#Percorre cada chave do dicionario com probabilidades divididas em intervalos
        cor=(key*qtd_camadas)-(qtd_camadas/2) # calculo que define o tom de cor no histograma
        try:
            valor=int(total_newprob[key]*base) #Pega o valor da probabilidade que está entre [0,1] e coloca ele no intervalo relativo ao tamanho da imagem

        except:
            valor=0
        for i,linha in enumerate(lista):#Percorre cada linha da imagem em preto que foi criada anteriormento
            inicio=key*qtd_camadas #define o inicio do intervalo onde será aplicada
            fim=inicio+qtd_camadas  #define o fim do intervalo onde será aplicada

            if fim >255:
                fim=255

            for subint in range(inicio,fim): #Percorre o intervalo de cada valor, para preencher a imagem
                if valor-i>0:

                    lista[i][subint]=cor



    # lista.reverse()

    raw_input("Pressione para visualizar o histograma, plotado como uma imagem\n\n")

    mostraImagem(lista)

print("Todas as funções utilizadas fizeram uso apenas de funções essenciais das bibliotecas matplotlib e numpy\n Toda a lógica, inclusive a plotagem do histograma foi implementado manualmente, como pode ser visualizado o código no código fonte.")
try:
    intervalo = input("Pra ter uma melhor visualização, \nEm quantos intervalos você deseja dividir a imagem?\nPreferencialmente números multiplos de 2!")
except:
    print("Você não definiu o valor, por padrão será adotado como 8.")
    intervalo=8
getHistogram(imgCopia,intervalo)
