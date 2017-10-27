import sys

casos=int(sys.stdin.readline())

for caso in range(casos):
	B=0
	R=0
	O=0
	K=0
	E=0
	N=0
	string=map(str,sys.stdin.readline())
	string.remove("\n")
	for letra in string:
		if letra =="B":
			B=B+1
		elif letra =="R":
			R=R+1
		elif letra =="O":
			O=O+1
		elif letra =="K":
			K=K+1
		elif letra =="E":
			E=E+1
		elif letra =="N":
			N=N+1
 
	if B==R and B==O and B==K and B==E and B==N:
		sys.stdout.write("No Secure\n")
	else:
		sys.stdout.write("Secure\n")