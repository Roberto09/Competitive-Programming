import sys
guardias_objetos= map(int,sys.stdin.readline().split())
valor_objetos=map(int,sys.stdin.readline().split())
valor_objetos.sort()
Suma=0
for objeto in range(guardias_objetos[1]):
	if valor_objetos[objeto]<0:
		Suma=Suma+(valor_objetos[objeto]*-1)
	else:
		break
sys.stdout.write(str(Suma)+"\n")