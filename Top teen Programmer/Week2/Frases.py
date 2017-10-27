import sys
import math
casos=int(sys.stdin.readline())
for caso in range(casos):
	oraciones=map(str,sys.stdin.readline().split())
	oracion1=oraciones[0]
	oracion2=oraciones[1]
	largo=len(oracion1)
	Diferentes=0
	for posicion in range(0,largo):
		if oracion1[posicion]!=oracion2[posicion]:
			Diferentes=Diferentes+1
	sys.stdout.write(str(Diferentes)+"\n")
