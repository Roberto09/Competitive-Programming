import random

x=int(raw_input())
casos_analizables=[]
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
		casos_analizables.append(sublista_numeros)
	if contador%4==0:
		
		M_GODZILLA=0
		M_MECHAGODZILLA=0
		contador_2=0

		for intervalo in casos_analizables:
			contador_2=contador_2+1
			if contador_2==1:
				for numero in intervalo:
					if numero>M_GODZILLA:
						M_GODZILLA=numero
			if contador_2==2:
				for numero in intervalo:
					if numero>M_MECHAGODZILLA:
						M_MECHAGODZILLA=numero

		if M_GODZILLA>M_MECHAGODZILLA:
			print("Godzilla")
		elif M_MECHAGODZILLA>M_GODZILLA:
			print("MechaGodzilla")
		else:
			print("incierto")

		casos_analizables=[]
