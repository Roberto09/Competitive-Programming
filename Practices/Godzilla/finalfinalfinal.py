import random
import sys

x=int(sys.stdin.readline())

for line in range(x):
	line1=sys.stdin.readline()
	line2=sys.stdin.readline()
	M_GODZILLA=max(map(int,sys.stdin.readline().split()))
	M_MECHAGODZILLA=max(map(int,sys.stdin.readline().split()))
	if M_MECHAGODZILLA>M_GODZILLA:
		print("MechaGodzilla")
	else:
		print("Godzilla")
	