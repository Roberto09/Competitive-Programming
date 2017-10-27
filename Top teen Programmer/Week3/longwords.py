import sys
casos=int(sys.stdin.readline())
for caso in range(casos):
	word=sys.stdin.readline().replace("\n","")
	largo=len(word)
	if largo>=10:
		sys.stdout.write(word[0]+str(largo-2)+word[largo-1]+"\n")

	else:
		sys.stdout.write(word+"\n")
