import sys
casos=int(sys.stdin.readline())
lista=[]
for caso in range(casos):
	sub_l=map(int,sys.stdin.readline().rstrip().split())
	sub_l.pop(0)
	for n in sub_l:
		lista.append(n)
lista=set(lista)

sys.stdout.write(str(len(lista))+"\n")
