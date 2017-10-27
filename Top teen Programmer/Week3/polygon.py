import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	x=int(sys.stdin.readline())
	a=2*x*x
	b=x*x
	c=2
	sys.stdout.write(str(a+b+c)+"\n")