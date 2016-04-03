from utils import imgReadAndCopy, mostraImagem
import cv2
__author__ = 'allan'
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

imgCopia,imgOriginal=imgReadAndCopy("Imagens/Fig0304(a)(breast_digital_Xray).tif")
for i,linha in enumerate(imgCopia):
    for j,col in enumerate(linha):



        imgCopia[i][j]=(255-col)


mostraImagem(imgOriginal)
mostraImagem(imgCopia)


# img=cv2.imread("Imagens/Fig0304(a)(breast_digital_Xray).tif")
#
# gs_imagem=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#
# imagem = (255-gs_imagem)
# cv2.imwrite("invertida.jpeg", imagem)
#
#
# plt.show()

