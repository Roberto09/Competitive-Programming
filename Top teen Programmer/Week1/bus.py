lista_datos=[]
Valor=0
for x in range(30):
	Valor=(2*Valor)+1
	lista_datos.append(Valor)

import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	x=int(sys.stdin.readline())
	sys.stdout.write(str(lista_datos[(x-1)])+"\n")
