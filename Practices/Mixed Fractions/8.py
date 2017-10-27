import sys
DO=True
while DO:
	fraccion=raw_input()
	if fraccion == "0 0":
		DO=False
	else:
		fraccion=map(int,fraccion.split(" "))

		x=fraccion[0]
		y=fraccion[1]

		p=int(x/y)
		q=x%y

		sys.stdout.write(str(p)+" "+str(q)+" / "+str(y)+"\n")