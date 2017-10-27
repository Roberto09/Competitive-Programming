import sys
semillas=int(sys.stdin.readline())
numeros=sorted(map(int,sys.stdin.readline().split()))
condition="YES"
separacion=numeros[1]-numeros[0]

for x in range(semillas-1):
	if (numeros[(x+1)]-numeros[x])!=separacion:
		condition="NO"
		break

sys.stdout.write(condition)


