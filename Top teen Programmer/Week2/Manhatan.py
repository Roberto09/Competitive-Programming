import sys
import math
casos=int(sys.stdin.readline())
for caso in range(casos):
	coordenadas=map(int,(sys.stdin.readline().split()))
	respuesta=int(math.fabs(coordenadas[0]-coordenadas[2])+math.fabs(coordenadas[1]-coordenadas[3]))
	sys.stdout.write(str(respuesta)+'\n')
