#3348
import sys
m_slides=[]

for slide in range(8):
	m_slides.append(int(sys.stdin.readline()))
for slide in range(8):
	m_slides.append(m_slides[slide])

slideI=0

MayorValor=0
for slide in range(8):
	valor=m_slides[slide]+m_slides[slide+1]+m_slides[slide+2]+m_slides[slide+3]
	slideI=slideI+1
	#print("-----"+str(sumatoria)+"-------")
	if valor>MayorValor:
		MayorValor=valor






sys.stdout.write(str(MayorValor)+"\n")

