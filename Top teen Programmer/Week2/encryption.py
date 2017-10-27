import math
import sys
palabra=raw_input()

largo_original=len(palabra)
largo=largo_original/2
npalabra1=(palabra[:largo])[::-1]
npalabra2=(palabra[-largo:])[::-1]

if largo_original%2==0:
	palabra_final=npalabra1+npalabra2
else:
	palabra_final=npalabra1+palabra[largo]+npalabra2

sys.stdout.write(palabra_final+"\n")