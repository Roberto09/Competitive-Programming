import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	numero=long(sys.stdin.readline())
	if numero%6==0:
		sys.stdout.write("YES\n")
	else:
		sys.stdout.write("NO\n")
