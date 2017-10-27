import sys
casos=int(sys.stdin.readline())
for x in range(casos):

	instruccion=map(str,sys.stdin.readline().split())
	n=int(instruccion[2])

	if instruccion[1]=="odd":#quito pares
		contador=0
		for x in range(0,int(instruccion[0])+1,2):
			if n==contador:
				sys.stdout.write(str(x)+"\n")
			contador=contador+1
	elif instruccion[1]=="even":#quitp impares
		contador=1
		for x in range(1,int(instruccion[0])+1,2):
			if n==contador:
				sys.stdout.write(str(x)+"\n")
			contador=contador+1