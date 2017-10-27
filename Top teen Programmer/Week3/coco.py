import sys
casos=int(sys.stdin.readline())
mayor=0
respuestas=[]
for caso in range(casos):
	resultados=map(int,sys.stdin.readline().split())
	resultados.sort()
	resultados.pop(0)
	resultados.pop((len(resultados)-1))
	sumatoria=sum(resultados)
	if caso==0:
		mayor=sumatoria
	elif sumatoria>mayor:
		mayor=sumatoria
	respuestas.append(str(caso+1)+" "+str(sumatoria)+"\n")
for respuesta in respuestas:
	sys.stdout.write(respuesta)

sys.stdout.write(str(mayor)+"\n")