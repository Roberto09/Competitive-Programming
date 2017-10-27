import sys
n=int(sys.stdin.readline())
if n>0:
	print((n*(n+1))/2)
else:
	n=n*-1
	print((((n*(n+1))/2)-1)*-1)