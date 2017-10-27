import sys
import math
casos=int(sys.stdin.readline())
respuestas=[]
for caso in range(casos):
	N_K=map(int,sys.stdin.readline().split())
	numero=N_K[0]
	k=N_K[1]
	suma=0.0
	for x in range(1,int(math.sqrt(numero)+1)):
		p_divisor=numero%x
		if p_divisor==0:
			if (x%k!=0):
				suma=suma+x
			otro_n=numero/x
			if otro_n%k!=0 and otro_n!=x:
				suma=suma+(otro_n)
	respuestas.append(suma)

for respuesta in respuestas:
	sys.stdout.write(str(int(respuesta))+"\n")


"""import sys
import math
casos=int(sys.stdin.readline())
for caso in range(casos):
	N_K=map(int,sys.stdin.readline().split())
	numero=N_K[0]
	k=N_K[1]
	suma=0.0
	for x in range(1,int(math.sqrt(numero)+1)):
		p_divisor=numero%x
		if p_divisor==0:
			if (x%k!=0):
				suma=suma+x
			otro_n=numero/x
			if otro_n%k!=0 and p_divisor!=x:
				suma=suma+(otro_n)

	sys.stdout.write(str(int(suma))+"\n")
"""