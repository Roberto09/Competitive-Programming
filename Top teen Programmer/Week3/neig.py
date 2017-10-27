import sys
numero=int(sys.stdin.readline())
numero=str(numero)
numero_reverse=numero[::-1]

sub_lista_num=""

n_final=""

hacer=True

for x in range(len(numero)-1):

	sub_lista_num=sub_lista_num+(numero_reverse[x])
	sub_lis_sort=sorted(sub_lista_num)

	for num in sub_lis_sort:
		if int(num)>int(numero_reverse[(x+1)]):
			n_final=numero[:(len(numero)-(len(sub_lista_num)+1))]
			n_final=n_final+str(num)
			sub_lis_sort.append(numero_reverse[(x+1)])
			sub_lis_sort.remove(num)
			sub_lis_sort=sorted(sub_lis_sort)
			for n in sub_lis_sort:
				n_final=n_final+n
			hacer=False
			break

	if hacer==False:
		break

if n_final!="":
	sys.stdout.write(n_final)

else:
	sys.stdout.write("0")







