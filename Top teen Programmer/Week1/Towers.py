#3351
import sys,string
letras_validas=['A','H','I','M','O','T','U','V','W','X','Y']

Torres=int(sys.stdin.readline())

for Torre in range(Torres):
	Nombre=sys.stdin.readline().replace("\n","")
	letras_en_lista=True
	Valida="NO\n"
	for letra in Nombre:
		if letra not in letras_validas:
			letras_en_lista=False
			break

	if letras_en_lista:
		if (Nombre[::-1])==Nombre:
			Valida="YES\n"

	sys.stdout.write(Valida)
