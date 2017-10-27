import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	MAYOR=0
	n=int(sys.stdin.readline())
	lista_numeros=[]
	suma_vacios=0
	for x in range(n):
		numeros=sum(map(int,sys.stdin.readline().split()))
		lista_numeros.append(numeros)
		if numeros>MAYOR:
			MAYOR=numeros

	suma_vacios=MAYOR*n-sum(map(int,lista_numeros))
	print (suma_vacios)

