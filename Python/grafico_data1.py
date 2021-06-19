import matplotlib.pyplot as plt
from sympy import *
init_printing()
var('a,b')

import numpy as np
from scipy.optimize import fsolve

with open('Filtro de Wien.txt') as f: #abre o arquivo
	lines = f.readlines() # converte as linhas do arquivo em strings
	x1 = [line.split()[0] for line in lines] # split converte cada linha em uma lista das palavras
	y1 = [line.split()[1] for line in lines]
	sigma_x1 = [line.split()[2] for line in lines] 
	sigma_y1 = [line.split()[3] for line in lines]

def string_float(): #funcao para converter strings em floats
	x = []
	y = []
	sigma_x = []
	sigma_y = []
	for i in x1:
		i = float(i)
		x.append(i)
	for j in y1:
		j = float(j)
		y.append(j)
	for k in sigma_x1:
		k = float(k)
		sigma_x.append(k)
	for l in sigma_y1:
		l = float(l)
		sigma_y.append(l)
	return x,y,sigma_x,sigma_y

def termo_chi_quadrado(a,b,i): #termo geral da serie chi-quadrado
	return ((string_float()[1][i]-a*(string_float()[0][i])-b)/(sigmay(a)[i]))**2

def chi_quadrado(a,b):  #serie chi-quadrado com todas as medidas
	chi_quadrado = 0
	i=0
	while i<len(string_float()[0]):
		chi_quadrado = chi_quadrado + termo_chi_quadrado(a,b,i)
		i=i+1
	return chi_quadrado

def sigmay(a): #incerteza no x convertida para incerteza no y atraves da propagacao, para cada (xi,yi)
	lista = []
	for j in range(len(string_float()[0])):
		lista.append(((string_float()[3][j])**2+(a*string_float()[2][j])**2)**(1/2))
		j=j+1
	return lista

f1 = Lambda(a, chi_quadrado(a,b)) #funcoes para depois derivarmos e igualarmos a zero
f2 = Lambda(b, chi_quadrado(a,b))

def a_b_valores():   # calculo dos parametros
	return nsolve([diff(f1(a),a),diff(f2(b),b)],[a,b],[80000,220000]) #resolve o sistema de equacoes

x = np.linspace(100,300,20)
y = a_b_valores()[0]*x+a_b_valores()[1]    #define a funcao que melhor se adequa aos pontos

plt.scatter(string_float()[0],string_float()[1],color='black',marker='.',s=30) #grafico dos pontos experimentais
plt.plot(x,y,'r--')
plt.title('Filtro de Wien',color='green')
plt.xlabel('Vp/i',color='red')
plt.ylabel('vx',color='red')
plt.show()