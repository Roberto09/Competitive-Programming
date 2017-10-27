import sys
casos=int(sys.stdin.readline())
import string
abc=map(str,string.ascii_uppercase)

for caso in range(casos):
	mensaje_final=str(caso+1)+" "
	mensaje=str(sys.stdin.readline())
	codigo=map(str,sys.stdin.readline())
	for caracter in mensaje:
		if caracter==" "or caracter=="\n":
			mensaje_final=mensaje_final+" "
		else:
			posicion=abc.index(caracter)
			mensaje_final=mensaje_final+(codigo[posicion])
	#sys.stdout.write(mensaje_final+"\n")
	print (mensaje_final)