import sys
import operator
casos=map(int,sys.stdin.readline().split())
dic_strings={}
lis_strings=[]
largo=casos[0]
for caso in range(casos[1]):
	string=sys.stdin.readline().rstrip()
	lis_strings.append(string)
	suma=0
	index=1
	for letter in string:
		for otherletter in range(index,largo):
			if letter>string[otherletter]:
				suma=suma+1
		index=index+1
	dic_strings[string]=suma

print (dic_strings)
print (lis_strings)

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



resultado=sorted(lis_strings, cmp=algoritmo)
for result in resultado:
	sys.stdout.write(result+"\n")

print(resultado)