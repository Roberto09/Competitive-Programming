#3039
import string,sys
abc=map(str,string.ascii_uppercase)

palabra=sys.stdin.readline().replace("\n","")

Total=1

for letra in palabra:
	valor=(abc.index(letra))+1
	Total=Total*valor

respuesta=str(Total%26)
if len(respuesta)==2:
	sys.stdout.write((respuesta))
else:
	sys.stdout.write("0"+respuesta)


