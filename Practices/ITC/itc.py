import sys
palabra=sys.stdin.readline().replace("\n","")
palabrar=palabra[::-1]
if palabrar==palabra:
	print("es un palindromo")
else:
	print("no es un palindromo")