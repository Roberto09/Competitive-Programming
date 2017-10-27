import sys
calificaciones=int(sys.stdin.readline())

diccionario={}


for calificacion in range(calificaciones):
	linea=map(str,sys.stdin.readline().split())
	diccionario[int(linea[0])]=linea[1]


orden=sorted(diccionario)

penalty_total=0
for minuto in orden:
	cal=diccionario[minuto]
	if cal=="AC":
		penalty_total=penalty_total+minuto
		break
	else:
		penalty_total=penalty_total+20
	if minuto==max(orden) and cal!="AC":
		penalty_total=0



sys.stdout.write(str(penalty_total))






"""
lista_casos=[]
Puntos_Menos=0
for calificacion in range(calificaciones):
	lista_casos.append(map(str,sys.stdin.readline().split()))
print (lista_casos)
"""






"""import sys
calificaciones=int(sys.stdin.readline())
lista_casos=[]
Puntos_Menos=0

for calificacion in range(calificaciones):
	caso=sys.stdin.readline()

	if calificacion==calificaciones-1:
		analizis=map(str,caso.split())
		if analizis[1]=="AC":
			Puntos_Menos=((calificaciones-1)*20)+int(analizis[0])
print(Puntos_Menos)
		
"""

