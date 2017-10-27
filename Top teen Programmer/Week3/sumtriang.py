import sys
import decimal
import math
numeros=map(long,sys.stdin.readline().split())
minimo=long(math.fabs(numeros[0]-numeros[1]))
maximo=long((numeros[0]+numeros[1])-1)

sumatoria_total=long((maximo*(maximo+1))/2)
sumatoria_resta=long((minimo*(minimo+1))/2)
sumatoria_final=long(sumatoria_total-sumatoria_resta)
sys.stdout.write(str(sumatoria_final)+"\n")
