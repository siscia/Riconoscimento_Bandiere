import Image
import numpy as np

from colori import colori_HSL_nome
from class_HSL import *
import time

"""
if __name__ == '__main__':
    im = Image.open('bandiere/cina.jpg')
    a = np.array(im)
    #print im.histogram()
    #b = list(a)
	#print b
	b = np.array([255, 251, 255])
	#print len(a)
	#print a[0]
	t1 = time.time()
	lista = singolo(a)
    
    colori_std = colori_HSL_nome
    
    #colori = colori_HSL_nome
	lista = [HSL(x) for x in lista]
    
	c = Clustering(colori_std, a)
	c.clusterizza()
	print c.cluster
"""


im = Image.open('bandiere/cina.jpg')
a = np.array(im)
#mappa = singolo(a)
a = a.tolist()
t1 = time.time()
totale = insieme(a)

#print a[259]
#dizio = swap_dictionary(dizio)
c = Clustering(colori_HSL_nome, totale)
c.clusterizza()
print c.cluster

