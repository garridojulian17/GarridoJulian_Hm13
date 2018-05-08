import numpy as np
from random import shuffle
import matplotlib.pyplot as plt



def sort_doors():
 	lista =["goat","goat","car"]
	shuffle(lista)
	return lista


def choose_door():
	N = [0,1,2]
	N_aleatorio = np.random.choice(N)
	return N_aleatorio



def reveal_door(lista,choice):

	for i in range (0,3):
		if (i!= choice):
			if (lista[i]=='goat'):
				lista[i] = "GOAT_MONTY"
				return lista

def finish_game(lista,choice,change):
	valorLista = 0
	#print lista
	if(change == False):
		
		valorLista =lista[choice]	
	if(change == True):
		a="GOAT_MONTY"
		for i in range (0,3):
			if(i != choice and lista[i]!=a):
				lista[i]
				valorLista =lista[i]
	return valorLista



def simulacion(change):
	prob = 0.0
	probabilidad =0.0
	for i in range (1000):
		a=sort_doors()
		b=choose_door()
		c=reveal_door(a,b)
		d=finish_game(c,b,change)
		if (d=="car"):
			prob += 1
			probabilidad = prob/1000
	return probabilidad
x= simulacion(True)
print "la probabilidad de obtener el premio sin cambiar la puerta  es ", x
y= simulacion(False)
print "la probabilidad de obtener el premio sin cambiar la puerta  es ", y








