from pandas import *
from numpy import *
import matplotlib.pyplot as plt
import json


def extract(fichier):
	with open(fichier, 'r') as f:
		test = f.readlines()
	i = 0
	y = -1
	tab = []
	while i < len(test):
		if test[i][0] == '-':
			i += 16
			y += 1
			tab += [[]]
		else:
			x = 0
			tmp = []
			while x < len(test[i])-2:
			    tmp += [int(test[i][x])]
			    x += 2
			tab[y] += [tmp]
			i += 1
	data = array(tab[2])
	s = DataFrame(data)
	return tab

def duree(L):
    return len(L)

def multi_infections(s):
	dic = {}
	for i in range(100):
		cpt = 0
		flag0 = 0
		flag1 = 0
		for infection in s[i]:
			if flag1 and flag0:
				if infection == 1:
					flag0 = 0
					cpt += 1
			elif flag1 and not flag0:
				if infection == 0:
					flag0 = 1
			else:
				if infection == 1:
					flag1 = 1
					cpt += 1
		try:
			dic[cpt] += 1
		except KeyError:
			dic[cpt] = 1
	return dic

def proportion(s):
	cpt = 0
	for i in range(100):
		for infection in s[i]:
			if infection == 1:
				cpt += 1
				break
	return cpt



if __name__ == '__main__':
	# infection periode
	# fichier = 'infecper_0.txt'
	# ind = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 999]


	# contagion periode
	# fichier = 'contaper_0.txt'
	# ind = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340]


	# nombre infecté
	# fichier = 'nbinfect_0.txt'
	# ind = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]


	# periode immunite
	# fichier = 'immunper_0.txt'
	# ind = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 999]


	# nombre de nodes
	# fichier = 'nombnode_0.txt'
	# ind = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]


	# travel distance
	fichier = 'travdist_0.txt'
	ind = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 999]

	col = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
	n = 1
	listdur = []
	listprop = []
	listmult = []
	for n in range(50):
		n += 1
		fichier = fichier[:9] + str(n) + '.txt'
		print(fichier)
		data = extract(fichier)
		dur = []
		prop = []
		mult = {}
		cpt = 0
		for i in range(len(data)):
			sim = DataFrame(array(data[i]))
			dur += [duree(sim)]
			prop += [proportion(sim)]
			tmp = multi_infections(sim)
			for key in tmp:
				try:
					mult[key] += tmp[key]
				except KeyError:
					mult[key] = tmp[key]
				cpt += tmp[key]
		listdur += [dur]
		listprop += [prop]
		for key in mult:
			mult[key] = mult[key] / cpt * 100
		listmult += [mult]

	# Durée d'épidémie
	tps = DataFrame(array(listdur), index=ind, columns= col)
	Plot_duree = tps.mean(axis = 1)
	with open(fichier[:9] + 'duree.json', "w") as f:
		json.dump(ind, f)
		f.write('\n')
		json.dump(Plot_duree.tolist(), f)
	prp = DataFrame(array(listprop), index=ind, columns=col)
	Plot_prop = prp.mean(axis = 1)
	# Proportion d'infection
	with open(fichier[:9] + 'prop.json', "w") as f:
		json.dump(ind, f)
		f.write('\n')
		json.dump(Plot_prop.tolist(), f)
	# Multi-infections
	df = DataFrame()
	for i in listmult:
		tmp = [()]
		tmpcol = []
		for key in i:
			tmp[0] += (i[key],)
			tmpcol += [key]
		print(tmp, tmpcol, tmp[0])
		dfnew = DataFrame(tmp, columns = tmpcol)
		df = df.append(dfnew, ignore_index=True)
	df['index'] = ind
	df = df.set_index('index')
	print(df)
	df.to_csv(fichier[:9] + 'multi.csv')
