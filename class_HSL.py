
#from colori import colori, colori_HSL_nome

class HSL():
	def __init__(self, code, rgb = True):
		if rgb == True:
			self.from_RGB(code)
		else:
			self.from_HSL(code)
		
	def from_HSL(self, hsl):
		self.h = hsl[0]
		self.s = hsl[1]
		self.l = hsl[2]
	
	def from_RGB(self, rgb):
		from colorsys import rgb_to_hls
		"""rgb = [x/255.0 for x in rgb]	
		max_rgb = max(rgb)
		min_rgb = min(rgb)
		
		self.l = (max_rgb + min_rgb) / 2
		
		if max_rgb == min_rgb:
			self.s = 0
			self.h = None
		else:
			delta = max_rgb-min_rgb
			if self.l < 0.5 :
				self.s = delta/(max_rgb+min_rgb)
			else:
				self.s = delta/(2-max_rgb-min_rgb)
				
			if rgb[0] == max_rgb:
				self.h = (rgb[1] - rgb[2]) / delta
				
			elif rgb[1] == max_rgb:
				self.h = 2 + (rgb[2] - rgb[0]) / delta
				
			else:
				self.h = 4 + (rgb[0] - rgb[1]) / delta
		
			self.h *= 60.0
		
			if self.h < 0:
				self.h += 360"""

		self.h, self.s, self.l = rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
		self.h *= 360
		
	def __str__(self):		
		return str(self.h) +'   '+ str(self.l*100) +'   '+ str(self.s*100)
	
	def distanza_euclidea(self, HSL):
		from math import sqrt
		try:
			d = sqrt((self.h - HSL.h)**2 + (self.l - HSL.l)**2 + (self.s - HSL.s)**2)
			return d
		except TypeError:
			d = sqrt((self.l - HSL.l)**2 + (self.s - HSL.s)**2 )
			return d
		
	def nearest(self, *arg):
		minimo = min(arg[0], key = lambda x: self.distanza_euclidea(x))
		return minimo 
	
	def gray(self):
		if 20 < self.l < 80 and self.s < 20:
			self.gray = True
		elif self.l > 95:
			self.white = True
		elif self.l < 5:
			self.black = True
			
		
class Clustering():	
	def __init__(self, centroidi, lista):
		self.centroidi = centroidi
		self.lista = lista
		self.cluster = dict()
	
	def clusterizza(self):
		for colore in self.lista:
			colore_HSL = colore.nearest(self.centroidi.keys())
			nome_colore = self.centroidi[colore_HSL]
			if nome_colore not in self.cluster:
				self.cluster[nome_colore] = self.lista[colore]
			else:
				self.cluster[nome_colore] += self.lista[colore]
				
def dizionarizza(array):
	import itertools as it
	dizio = dict()
	for _ in xrange(len(array)):
		Porta_c = it.chain(array[_])
		while True:
			try:
				chiave = Porta_c.next()
				chiave = tuple(chiave)
				if chiave not in dizio.keys():
					#print chiave
					dizio[chiave] = 0
			except StopIteration:
				for RGB in dizio.keys():
					tot_RGB = (array==RGB).sum()
					dizio[RGB] = tot_RGB
	return dizio
	
def singolo(array):
	import itertools as it
	mappa = list()
	for i in xrange(len(array)):
		for j in xrange(len(array[i])):
			a = list(array[i][j])
			if a not in mappa:

				mappa.append(a)
				
	return mappa
		

def insieme(array):
	dizio = dict()
	for x in array:
		for y in x:
			y = HSL(y)
			if not dizio.has_key(y):
				dizio[y] = 1
			else:
				dizio[y] += 1
			
	return dizio



def swap_dictionary(original_dict):
    return dict([(v, k) for (k, v) in original_dict.iteritems()])
"""
for nome,colore in colori.items():
	colori[nome] = HSL(colore, False)

colori = colori_HSL_nome
a = {HSL([45,45,250]):253, HSL([54,78,63]):53, HSL([58,78,63]):3 }

c = Clustering(colori_HSL_nome, a)
c.clusterizza()
print c.cluster

"""

