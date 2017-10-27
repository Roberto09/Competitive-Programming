import sys
resultados=[]
def algoritmo(str1, str2):
    if dic_strings[str1]>dic_strings[str2]:
        return 1
    elif dic_strings[str1]<dic_strings[str2]:
        return -1

    elif str1>str2:
        return 1
    elif str1<str2:
        return -1
    else:
        return 0

stop=[0,0]
while True:
	casos=map(int,sys.stdin.readline().split())
	if casos==stop:
		break
	dic_strings={}
	lis_strings=[]
	largo=casos[0]
	for caso in range(casos[1]):
		string=sys.stdin.readline().rstrip()
		lis_strings.append(string)
		suma=0
		index=0
		for letter in string:
			for otherletter in range(index,largo):
				if letter>string[otherletter]:
					suma=suma+1
			index=index+1
		dic_strings[string]=suma

	resultado=sorted(lis_strings, cmp=algoritmo)
	resultados.append(resultado)


largotl=len(resultados)
for resu in resultados:
	for r in resu:
		sys.stdout.write(r+"\n")
	largotl=largotl-1
	if largotl!=0:
		print("")

