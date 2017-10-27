import sys
binario=str(sys.stdin.readline())
largo=len(binario)-1

if (largo+1)%3==0:
	binario="0"+binario
elif (largo+2)%3==0:
	binario="00"+binario

traduccion=["000","001","010","011","100","101","110","111"]

numero_final=""
n=0
for x in range(len(binario)/3):
	numero=(binario[(x*3):(x*3+3)])
	numero_final=numero_final+str(traduccion.index(numero))

print(numero_final)
