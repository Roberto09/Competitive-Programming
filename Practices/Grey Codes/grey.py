import sys

NK=map(int,(sys.stdin.readline().split()))

N=NK[0]
K=NK[1]
VI=0
VF=(2 ** N)/2
espejo=False
binario=""


for exp in range(N-1,-1,-1):
	if K>=VI and K<VF: #entre 0 y 7
		VF=VF-(2 ** (exp))
		if espejo==False:
			binario="0"+binario
		
		else:
			binario="1"+binario
		espejo=False


	else: #entre 8 y 15
		VI=VF
		VF=VI+ (2 ** (exp))
		if espejo==False:
			binario="1"+binario

		else:
			binario="0"+binario
		espejo=True

	print ("iteracion: " + str(exp) + " intervalo: " + str(VI) + " a " + str(VF) )

print(binario)


	








"""
binario=""
variable=K
for exp in range(N-1,-1,-1):
	elevacion= (2 ** exp)
	#print (elevacion)
	if variable>=elevacion:
		binario="1"+binario
		variable=K-elevacion
	else:
		binario="0"+binario


print (binario)

"""