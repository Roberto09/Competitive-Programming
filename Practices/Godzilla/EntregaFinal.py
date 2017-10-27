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


def ganador(Godzilla,Megagozilla):
	
	if Godzilla == Megagozilla:
		ganador=random.choice(["Godzilla","Megozilla"])
		print ("incierto")
	elif Godzilla>Megagozilla:
		print ("Godzilla")
	else:
		print("MechaGodzilla")

def algoritmo_mayor_menor():
	mayor_godzilla=0
	mayor_megagodzilla=0
	repeticion=0
	for intervalo in casos_analizables:
		repeticion=repeticion+1

		for numero in intervalo:
			if repeticion%2 != 0:
				if int(numero)>mayor_godzilla:
					mayor_godzilla=numero
					#print ("xxxxx"+ str(mayor_godzilla))

			if repeticion%2 == 0:
				if int(numero)>mayor_megagodzilla:
					mayor_megagodzilla=numero

		if repeticion%2 == 0:

			ganador(mayor_godzilla,mayor_megagodzilla)

			mayor_godzilla=0
			mayor_megagodzilla=0

algoritmo_mayor_menor()

