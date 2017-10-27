nm=raw_input()
listanm=(map(int,nm.split()))

xyc=raw_input()
listaxyc=(map(int,xyc.split()))

x=listaxyc[0]
y=listaxyc[1]

lista_cordenadas=[]
for n in range(listaxyc[2]):
	cordenada=raw_input()
	lista_cordenadas.append(cordenada)


for cordenada in reversed(lista_cordenadas):
	cordenada_=cordenada.split(" ")
	movimiento= int(cordenada_[1])
	orientacion=cordenada_[0]


	if orientacion=="N":
		x=x+movimiento

	if orientacion=="S":
		x=x-movimiento

	if orientacion=="E":
		y=y-movimiento

	if orientacion=="W":
		y=y+movimiento

print(str(x)+" "+str(y))