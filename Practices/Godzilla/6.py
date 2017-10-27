import random

lista_respuestas=[]



x=int(raw_input())
contador=0
for line in range(x*4):
	contador=contador+1
	line=raw_input()
	if line =="" or contador==2 or (contador-2)%4==0:
		continue
	else:
		numeros=line.split(" ")
		sublista_numeros=[]
		for numero in numeros:
			sublista_numeros.append(int(numero))
		if (contador+1)%4==0:
			M_GODZILLA=max(map(int,sublista_numeros))
		else:
			M_MECHAGODZILLA=max(map(int,sublista_numeros))
	if contador%4==0:
		if M_GODZILLA>M_MECHAGODZILLA:
			lista_respuestas.append("Godzilla")
		elif M_MECHAGODZILLA>M_GODZILLA:
			lista_respuestas.append("MechaGodzilla")
		else:
			lista_respuestas.append("incierto")

for respuesta in lista_respuestas:
	print(respuesta)
