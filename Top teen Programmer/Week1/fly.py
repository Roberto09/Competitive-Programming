import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	inpt=map(float,sys.stdin.readline().split())
	Resultado=(inpt[0]/(inpt[1]+inpt[2]))*inpt[3]
	Resultado="%.2f" % Resultado
	sys.stdout.write((Resultado)+"\n")