#3348
import sys
N_K=map(float,sys.stdin.readline().split())
n=(N_K[0])-1
Combates=(n*(n+1))/2
ganadas_posibles=Combates/(N_K[0])
if (N_K[1])<=ganadas_posibles:
	sys.stdout.write(str(int((N_K[0])*(N_K[1])))+"\n")
else:
	sys.stdout.write("-1\n")
