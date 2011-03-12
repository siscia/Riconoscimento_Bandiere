"""
prova per sviluppo iphone.py
"""
import sqlite3
import Image
import ImageDraw

def prendi_elenco(file_in):
	info = dict()
	file_input = open(file_in, "r")
	for line in file_input:
		line = line.split(' - ')
		info['nazione'] = line[0].decode('utf-8')
		info['capitale'] = line[1].decode('utf-8')
		info['colori'] = None
		memorizza(info)
	return 0
		
def memorizza(info):
	conn = sqlite3.connect('/home/simo/Scrivania/nazioni/nazioni.db')
	c = conn.cursor()
	c.execute("insert into nazioni(nazione,capitale,colori) values (?,?,?)", (info['nazione'], info['capitale'], info['colori']))
	conn.commit()
	c.close()

#prendi_elenco("nazioni_-_capitali.txt")

def analizzaBandieraGIF(bandiera):
	im = Image.open('bandiere/'+bandiera)#.convert("P", palette = Image.ADAPTIVE, colors = 100)	
	print im.histogram()
	colori = im.getcolors()
	media = sum(x[0] for x in colori)/len(colori)
	risultato = filter(lambda x: x[0] > media, colori)
	if len(risultato) == 1:
		return secondo_picco(colori)
	return risultato

def secondo_picco(lista):
	return sorted(lista,reverse = True)[:2]

def quadrati(lista,dim):	
	def colora(im, dim, colore):
		for j in xrange(dim):
			for i in xrange(dim):
				#print colore
				im.putpixel((i,j),colore)
		return im
		
	im = Image.new("P", (dim,dim))
	for info in lista:
		colora(im, dim, info[1]).show()


"""def analizzaBandieraGIF1(bandiera):
	im = Image.open(bandiera)
	if im.format != 'GIF':
		return im.getcolors()			
	colori = im.getcolors()	
	#return colori	
	media = sum(colori[0])/len(colori)
	risultato = filter(lambda x: x[0] > media, colori)
	return risultato,media"""
		
		
"""print analizzaBandieraGIF('algeria.GIF')
print analizzaBandieraGIF('cina.GIF')
print analizzaBandieraGIF('emirati_arabi_uniti.GIF')
quadrati(analizzaBandieraGIF('emirati_arabi_uniti.GIF'),50)
"""
#print analizza_bandiera('REDDY.jpeg')

def analizzaBandieraGIF2(bandiera):
	im = Image.open('bandiere/'+bandiera)#.convert("P")
	im.show()
	print im.histogram()
	colori = im.getcolors()
	media = sum(x[0] for x in colori)/len(colori)
	#risultato = filter(lambda x: x[0] > 1000, colori)
	risultato = colori
	risultato = unisci(risultato)
	if len(risultato) == 1:
		return secondo_picco(colori)
	return risultato
	
def near(x,y, distanza = 3):
	if 0 < x-y <= 3:
		return True
	else:
		return False

def unisci(lista):
	lista = [list(x) for x in lista]
	print lista
	print
	for x in lista:
		for j in lista:
			if near(x[1],j[1]) and x != j:
				ind = lista.index(x)
				lista[ind][0] += j[0]
				
				lista.remove(j)			
	return lista
	
#print analizzaBandieraGIF('cina.jpg')

im = Image.open('bandiere/cina.jpg')
#print im.histogram()
lis = dict()
x,y = im.size
for i in xrange(x):
	for j in xrange(y):
		colo = im.getpixel((i,j))
		if colo in lis.keys():
			lis[colo] += 1
		else:
			lis[colo] = 1
		
"""for k in sorted(lis.keys()):
	print k, "-->", lis[k]"""
	
print sorted(lis.items(), key=lambda(k,v):(v,k))

