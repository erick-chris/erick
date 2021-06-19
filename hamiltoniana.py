# montando a hamiltoniana de uma particula em caixa de comprimento L, potencial V(x) = ax/L
# encontrando a densidade de probabilidade de uma particula em um poço potencial assimetrico

import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg
import math

#constantes
L = 5*10**(-10)        # comprimento da caixa (em metros)
a = 10                 # em eV 
h1 = 1.0546*10**(-34)  # constante de Planck reduzida (em J.s)
h2 = 6.582*10**(-16)   # constante de Planck reduzida (em eV.s)
M = 9.1094*10**(-31)   # massa do eletron (em kg)

def hamil_element(m,n): #calculo de Hmn para n,m inteiros arbitrarios, para um eletron confinada na caixa
	if m != n:
		if (m % 2 == 0 and n%2==0):
			H = 0
		elif (m%2 != 0 and n%2 !=0):
			H = 0
		else:
			H = -(8*a*m*n)/(math.pi*(m**2-n**2))**2
	else:
		H = a/2 + (h1*h2*(math.pi*n)**2)/(2*M*L**2)
	return H

def hamil_matrix():  #matriz hamiltoniana, gerada com os termos Hmn. Matriz 3x3.
	H_matrix = []
	for i in range(1,21):
		lista = []
		for j in range(1,21):
			lista.append(hamil_element(i,j))
		H_matrix.append(lista)
	return H_matrix

def eigen_values():  #autovalores (energias) relacionadas a matriz hamiltoniana gerada. Aqui sao obtidos 3 autovalores.
	A = np.array(hamil_matrix(),dtype=float)
	w, v = linalg.eig(A)
	return w

def eigen_vectors(): #autovetores (autoestados) relacionadas a matriz hamiltoniana gerada. Os autovetores possuem 3 coordenadas. 
	A = np.array(hamil_matrix(),dtype=float)
	c, d = linalg.eig(A)
	return d[0],d[1],d[2]

#reta em x
t = np.arange(0,5*10**(-10),5*10**(-12))

y1 = 0 #valores iniciais
y2 = 0
y3 = 0
i=0
while i<20: # nesse laço é somado os termos de Fourier (senos) com as coordenadas dos autovetores obtidos como coeficientes.
	y1 = y1 + math.sqrt(2/L)*eigen_vectors()[0][i]*np.sin(math.pi*(i+1)*t/L)
	y2 = y2 + math.sqrt(2/L)*eigen_vectors()[1][i]*np.sin(math.pi*(i+1)*t/L)
	y3 = y3 + math.sqrt(2/L)*eigen_vectors()[2][i]*np.sin(math.pi*(i+1)*t/L)
	i+=1

#psi ao quadrado
z1 = y1**2 
z2 = y2**2
z3 = y3**2

# graficos
plt.plot(t,z1,'r')
plt.plot(t,z2,'g')
plt.plot(t,z3,'b')
plt.title('Particle in a box')
plt.legend(['ground state','first excited state','second excited state'])
plt.xlabel('x')
plt.ylabel('phi^2')
plt.show()