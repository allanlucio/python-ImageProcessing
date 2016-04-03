# coding=utf-8
from numpy.core.multiarray import arange

__author__ = 'allan'


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def imgReadAndCopy(nome):
    img=mpimg.imread(nome,0)
    imgcopy = img.copy()
    return imgcopy.tolist(),img.tolist()


def mostraImagem(matriz):
    limite=255*150
    imgplot = plt.imshow(np.array(matriz), cmap='Greys_r',extent=[0,limite,limite,0])

    plt.gca().invert_yaxis()
    frame=plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    plt.xlabel("Tonalidade de cor")
    plt.ylabel("Frequencia")

    plt.show(block=True)