import sys
import math
import decimal
x=True
while(x):
	numero=long(sys.stdin.readline())
	if numero==0:
		break
	else:
		raiz=decimal.Decimal(1+(8*numero)).sqrt()
		resultado=raiz%1
		if resultado>0:
			sys.stdout.write("NO\n")
		else:
			sys.stdout.write("YES\n")