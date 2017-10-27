import sys

def alg(p):
	z=True
	for n in range(2,(p/2)+1):
		y=float(p)%float(n)
		if y != 0:
			continue
		else:
			z=False
			break
	return z

"""for x in range(ninicial,nfinal):
	if alg(x):
		print(x)"""

casos=int(sys.stdin.readline())
for caso in range(casos):
	respuesta=0
	numero=int(sys.stdin.readline())
	for x in range(2,numero+1):
		if alg(x):
			#print(x)
			if numero%x==0:
				respuesta=respuesta+1

	sys.stdout.write(str(respuesta)+'\n')