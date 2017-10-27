import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	matriz=[]
	lineas=int(sys.stdin.readline())
	for x in range(lineas):
		lista=[]
		linea=sys.stdin.readline()
		for car in linea:
			if car=='.':
				lista.append(True)
			if car=='#':
				lista.append(False)
		matriz.append(lista)
	print(matriz)


	matriz_vert=[]

	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			matriz_vert.append(matriz[x][y])


print(matriz_vert)


