# coding: utf-8
# modelo SIR (susceptíveis, infectados e recuperados)
# usando odeint

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parâmetros
l = 0.001 #taxa de infeccao
g = 0.05 #taxa de recuperacao

def SIR(y,t):
	y_a, y_b, y_c = y
	
	dy_adt = -l*(y_a)*(y_b)	
	dy_bdt = l*(y_a)*(y_b)-g*(y_b)
	dy_cdt = g*(y_b)

	return [dy_adt, dy_bdt, dy_cdt]

#time domain
t_span = np.linspace(0,200,100)

#condições iniciais
S0 = 99
I0 = 1
R0 = 0

y0 = [S0,I0,R0]

solution = odeint(SIR, y0, t_span)

plt.plot(t_span, solution[:, 0], label='susceptíveis')
plt.plot(t_span, solution[:, 1], label='infectados')
plt.plot(t_span, solution[:, 2], label='recuperados')
plt.legend(bbox_to_anchor=(0.71, 0.57), loc='upper left', borderaxespad=0.)
plt.title("Simulação de epidemia: modelo SIR")
plt.xlabel('tempo')
plt.ylabel('casos')
plt.show()