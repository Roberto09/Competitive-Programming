import sys
casos=int(sys.stdin.readline())

for x in range(casos):
	caso=map(float,sys.stdin.readline().split())
	solucion=caso[0]/caso[1]
	sys.stdout.write(str(format(solucion,".2f"))+"\n")