"""Godzilla vs Megagozilla"""
import random


#interpretacion de datos
def interpretar_datos(Archivo, Remove):
	lista_strings=[]

	with open(Archivo,"r") as Datos:
		for line in Datos:
			line= line.replace(Remove,"")
			lista_strings.append(line)


	lista_datos=[]

	for string in lista_strings:

		if string=="":
			continue
		else:
			grupo_numeros = string.split(" ")

			lista_numeros=[]

			for numero in grupo_numeros:
				numero= int(numero)
				lista_numeros.append(numero)

			lista_datos.append(lista_numeros)

	return lista_datos
lista_datos=interpretar_datos("Datos.txt","\n")

#print(lista_datos)

nCasos=lista_datos[0]
nCasos=nCasos[0]

casos_analizables=[]

print (casos_analizables)

def segregacion_casos_analizables():

	contador=nCasos
	inicia_intervalo=2



	while contador>0:
		casos_analizables.append(lista_datos[inicia_intervalo])
		casos_analizables.append(lista_datos[inicia_intervalo+1])
		inicia_intervalo=inicia_intervalo+3
		contador=contador-1

	print(casos_analizables)
segregacion_casos_analizables()

def ganador(Godzilla,Megagozilla):
	
	if Godzilla == Megagozilla:
		ganador=random.choice(["Godzilla","Megagozilla"])
		print ("El ganador fue: "+ganador)
	elif Godzilla>Megagozilla:
		print ("El ganador fue Godzilla")
	else:
		print("El ganador fue Mega Godzilla")

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


