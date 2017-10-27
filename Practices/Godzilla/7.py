import random
import sys

#Lee la primera linea de codigo 
x=int(sys.stdin.readline())

#contador de renglones
contador=0
#for para pedir datos
for line in range(x*4):
	contador=contador+1
	line=sys.stdin.readline()
	if line =="" or contador==2 or (contador-2)%4==0:
		continue
	else:
		sublista_numeros=map(int,line.split(" "))
		if (contador+1)%4==0:
			M_GODZILLA=max(map(int,sublista_numeros))
		else:
			M_MECHAGODZILLA=max(map(int,sublista_numeros))
	if contador%4==0:
		if M_GODZILLA>M_MECHAGODZILLA:
			print("Godzilla")
		elif M_MECHAGODZILLA>M_GODZILLA:
			print("MechaGodzilla")
		else:
			print("incierto")
