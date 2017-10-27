"""import sys

casos=int(sys.stdin.readline())

lista_numeros=[]

for caso in range(casos):
	numero=sys.stdin.readline()
	if numero[0]=="-":
		del numero [0]
	numero=map(str, numero)
	lista_numeros.append(numero)

print (lista_numeros)



"""



"""import sys
casos=int(sys.stdin.readline())
numeros_ant=[]
cantidad=0
for caso in range(casos):
	numero=int(sys.stdin.readline())
	sumatoria=0
	largo=0

	for n in str(numero):
		sumatoria=sumatoria+int(n)
		largo=largo+1

	valor=str(largo)+str(sumatoria)

	if valor not in numeros_ant:
		cantidad=cantidad+1
		numeros_ant.append(valor)

sys.stdout.write(str(cantidad)+"\n")
"""

import sys
casos=int(sys.stdin.readline())
lista_numeros=[]
cantidad=0
for caso in range(casos):
	numero=sys.stdin.readline()
	C0=0
	C1=0
	C2=0
	C3=0
	C4=0
	C5=0
	C6=0
	C7=0
	C8=0
	C9=0

	for n in numero:
		if n=='0':
			C0=C0+1
		if n=='1':
			C1=C1+1
		if n=='2':
			C2=C2+1
		if n=='3':
			C3=C3+1
		if n=='4':
			C4=C4+1									
		if n=='5':
			C5=C5+1
		if n=='6':
			C6=C6+1
		if n=='7':
			C7=C7+1
		if n=='8':
			C8=C8+1
		if n=='9':
			C9=C9+1
	nfinal=(C0,C1,C2,C3,C4,C5,C6,C7,C8,C9)
	lista_numeros.append(nfinal)


lista=list(set(lista_numeros))
sys.stdout.write(str(len(lista))+"\n")

"""
import sys

nllaves= int(sys.stdin.readline())
llaves=[]
x=0
for llave in range(nllaves):
	numero=map(str,(sys.stdin.readline().replace("\n","")).replace("-",""))
	numero.sort()
	nfinal=""
	for n in numero:
		nfinal=nfinal+n
	llaves.append(long(nfinal))

llaves_final=list(set(llaves))
sys.stdout.write(str(len(llaves_final))+"\n")"""

"""a=10
b=32
c=4
tupla=(a,b,c)
print (tupla)"""