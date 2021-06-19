def primo(a):
	lista = []
	s = False
	for i in range(1,a+1):
		if a%i==0:
			lista.append(i)
	if len(lista)>2:
		s = False
	elif len(lista)==2:
		s = True
	return s

def quant_primos(n):
	j=0
	lista2=[]
	b = 1
	while b<(2*n)**10:
		b+=1
		if primo(b)==True:
			lista2.append(b)
			j+=1
			if j==n:
				break
	return lista2
