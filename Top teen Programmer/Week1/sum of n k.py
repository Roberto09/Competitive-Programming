import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	N_K=map(int,sys.stdin.readline().split())
	N=N_K[0]
	K=N_K[1]

	fac1=1
	fac2=1
	fac3=1
	#parte 1
	for x in range(2,(N+K)):
		fac1=fac1*x
	#parte 2
	for x in range(2,(N+1)):
		fac2=fac2*x
	#parte 3
	for x in range(2,K):
		fac3=fac3*x

	respuesta=((fac1)/(fac2*fac3))%1000000007
	sys.stdout.write(str(respuesta)+"\n")
