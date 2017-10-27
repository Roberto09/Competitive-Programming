import sys
import math
n=raw_input()
sumas=1
while True:
	N=int(n)
	listan=sorted(n)
	M=""
	for n in listan:
		M=M+n
	M=int(M)

	resta=N-M
	if resta==0:
		break
	else:
		sumas=sumas+1
		n=str(resta)

sys.stdout.write(str(sumas)+"\n")

