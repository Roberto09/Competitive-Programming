import sys
import math
def pitagoras(a,b):
	return math.sqrt(((a*a)+(b*b)))
casos=int(sys.stdin.readline())
for caso in range(casos):
	a=float(sys.stdin.readline())
	a2=a*1.5
	a3=a/3
	a4=a/2

	DM=pitagoras(a,a2)
	MN=pitagoras(a4,a3)
	DN=DM-MN
	resultado="%.4f" %((1/(DM*DM))+(1/(DN*DN)))
	sys.stdout.write(str(resultado)+"\n")
