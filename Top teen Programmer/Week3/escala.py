import sys
casos=int(sys.stdin.readline())
respuestas=[1,2,3,4,5]
respuestas2=[2,3,4,5,6]
for caso in range(casos):
	numeros=map(int,sys.stdin.readline().split())
	numeros.sort()
	if numeros==respuestas or numeros==respuestas2:
		sys.stdout.write("Y\n")
	else:
		sys.stdout.write("N\n")