import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	numero=int(sys.stdin.readline())
	encontrado=False
	while encontrado==False:
		numero=numero+1
		numerostr=str(numero)
		reversastr=numerostr[::-1]
		if reversastr==numerostr:
			sys.stdout.write(numerostr+"\n")
			break
		else:
			continue