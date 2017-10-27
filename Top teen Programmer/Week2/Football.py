import sys
import math
juegos_gcompar=map(int,sys.stdin.readline().split())
diferencias=[]
ganados=0
empatados=0
perdidos=0
for juego in range(juegos_gcompar[0]):
	resultado=map(int,sys.stdin.readline().split())
	diferencia=resultado[0]-resultado[1]

	if diferencia<0:
		diferencias.append(diferencia)
		perdidos=perdidos+1

	elif diferencia==0:
		empatados=empatados+1
		diferencias.append(diferencia)

	else:
		ganados=ganados+1

diferencias=sorted(diferencias, reverse=True)

#print(diferencias)

gastar=juegos_gcompar[1]
#print(goles_comprados)

#algoritmo

for dif in diferencias:
	if gastar>0:
		if dif+gastar>0:
			gastar=(gastar+dif)-1
			ganados=ganados+1
			if dif==0:
				empatados=empatados-1
			else:
				perdidos=perdidos-1
		elif dif+gastar==0:
			gastar=(gastar+dif)
			empatados=empatados+1
			perdidos=perdidos-1
		else:
			break
	else:
		break


puntos_total=(ganados*3)+empatados
sys.stdout.write(str(puntos_total)+"\n")