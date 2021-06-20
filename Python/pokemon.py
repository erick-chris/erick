#captura de pokemons
#representacao matricial
#funçoes, listas, matrizes, arquivos, condicionais, laços, etc

import math

DELTA_T = 0.1
GRAVIDADE = 2

def leArquivo(nomeArquivo = 'entrada.txt'):
	arq = open(nomeArquivo)
	matriz = []
	for linha in arq:
		lista = linha.split()
		if len(lista)==2: #primeira linha do arquivo
			line = []
			for elemento in lista:
				line.append(int(elemento))
		else: #restante das linhas
			line = []
			numeros = lista[1:]
			line.append(lista[0])
			for elemento in numeros:
				line.append(int(elemento))
		matriz.append(line)
	arq.close()
	return matriz

def populaMatriz(matriz,pokemons):
	for i in range(0,len(matriz)):
			for j in range(0,len(matriz[0])):
				matriz[i][j]='.' #troca elementos da matriz por ponto
	for k in range(1,len(pokemons)):
		pokem = criaMatriz(2*int(pokemons[k][1])+1,2*int(pokemons[k][1])+1) #cria matriz dos pokemons
		matriz[len(matriz) - int(pokemons[k][3]) -1][int(pokemons[k][2])]=pokem[int(pokemons[k][1])][int(pokemons[k][1])]=k #centro do pokemon
		for i in range(0,len(pokem)):
			for j in range(0,len(pokem[0])):
				pokem[i][j]=k #representa o pokemon por um numero
		r=0
		while r<int(pokemons[k][1]): #preenche pokemon
			r+=1
			matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1][int(pokemons[k][2])+r]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1][int(pokemons[k][2])-r]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+r]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-r]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-r]=pokem[0][0]
			matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+r]=pokem[0][0]
			if int(pokemons[k][1])==2:
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-2]=pokem[0][0]
			if int(pokemons[k][1])==3:
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-3]=pokem[0][0]
			if int(pokemons[k][1])==4:
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])+4]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])+4]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-1]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-2]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-3]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1+r][int(pokemons[k][2])-4]=pokem[0][0]
				matriz[len(matriz) - int(pokemons[k][3]) - 1-r][int(pokemons[k][2])-4]=pokem[0][0]
	return matriz

def removePokemon(matriz,id,pokemons):
	populaMatriz(matriz,pokemons)
	for i in range(0,len(matriz)):
		for j in range(0,len(matriz[0])):
			if matriz[i][j]==id:
				matriz[i][j]='.'
	return matriz

def criaMatriz(m,n):
	A = []
	for i in range(m):
		linha=[]
		for j in range(n):
			linha.append(0)
		A.append(linha)
	return A

def imprimeMatriz(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			print(matriz[i][j], end='')
		print()

def atualizaPosicao(x,y,vx,vy,dt=DELTA_T):
	x=x+vx*dt
	y=y+vy*dt-(GRAVIDADE*dt**2)/2
	return x,y,round(x),round(y)

def atualizaVelocidade(vx,vy,dt=DELTA_T):
	vx=vx
	vy=vy-GRAVIDADE*dt
	return vx, vy

def grau2Radiano(theta):
	rad = (theta*(math.pi))/180
	return rad

def main():
	nome = input('Digite o nome do arquivo: ')
	N = int(input('Digite o numero N de pokebolas: '))
	pokemon = leArquivo(nome)
	matriz = criaMatriz(pokemon[0][0],pokemon[0][1])
	Npokemons=int(len(pokemon)-1) #pokemons disponiveis
	xt= int(input('Digite a coordenada x do treinador: '))
	print('pokebolas disponiveis = ',N)
	print('Estado atual do jogo:')
	populaMatriz(matriz,pokemon)
	matriz[len(matriz)-1][xt]='T'
	imprimeMatriz(matriz) # imprime a matriz contendo os pokemons e o treinador
	while N>0 and Npokemons>0:
		N-=1
		v = int(input('Digite a velocidade de lancamento em m/s: '))
		theta = int(input('Digite o angulo de lancamento em graus: '))
		vx = v*(math.cos(grau2Radiano(theta))) # velocidade inicial em x
		vy = v*(math.sin(grau2Radiano(theta))) #velocidade inicial em y
		x = xt #posicao da pokebola em x
		y = 0 #posicao da pokebola em y
		jogo=True
		while y>=0 and x>=0 and x<=(len(matriz[0])-1) and jogo: #simulacao do lancamento da pokebola
			vx = atualizaVelocidade(vx,vy,dt=DELTA_T)[0]
			vy = atualizaVelocidade(vx,vy,dt=DELTA_T)[1]
			x = atualizaPosicao(x,y,vx,vy,dt=DELTA_T)[2]
			y = atualizaPosicao(x,y,vx,vy,dt=DELTA_T)[3]
			matriz[len(matriz)-y-1][x]='o' #arrumar coordenadas da pokebola
			if matriz[len(matriz)-y-1][x]==matriz[len(matriz)-1][xt]:
				matriz[len(matriz)-y-1][x]='T' #mantem a posicao do treinador
			for k in range(1,len(pokemon)):
				for i in range(len(matriz)-int(pokemon[k][3])-1-int(pokemon[k][1]),len(matriz)-int(pokemon[k][3])+int(pokemon[k][1])):
					for j in range(int(pokemon[k][2])-int(pokemon[k][1]),int(pokemon[k][2])+int(pokemon[k][1])+1):
						if matriz[len(matriz)-y-1][x]==matriz[i][j]: 
							jogo=False	# a simulacao para quando a pokebola encontra o pokemon
		print('Representacao grafica do lancamento:')	
		imprimeMatriz(matriz)  #imprime a matriz agora contendo a trajetoria da pokebola
		if jogo==False:	 #exibe uma mensagem se algum pokemon foi capturado
			for k in range(1,len(pokemon)):
				if matriz[len(matriz)-round(y)-2][round(x)]==k:  
					print('Um',pokemon[k][0],'foi capturado!')	
					Npokemons-=1
					matriz[len(matriz)-1][round(x)]='T'
					print('pokebolas disponiveis = ',N+1)
					print('Estado atual do jogo:')
					imprimeMatriz(removePokemon(matriz,k,pokemon)) # imprime a matriz contendo os pokemons e o treinador
		else:
			print('O lancamento nao capturou pokemon algum')
			if N>0:
				xt=int(input('Digite a coordenada x do treinador: '))
				print('pokebolas disponiveis = ',N+1)
				print('Estado atual do jogo:')
				populaMatriz(matriz,pokemon)
				matriz[len(matriz)-1][xt]='T'
				imprimeMatriz(matriz) # imprime a matriz contendo os pokemons e o treinador
	if Npokemons==0:
		print('Parabens! Todos pokemons foram capturados')
	else:
		print('Jogo encerrado')