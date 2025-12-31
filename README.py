# C.-Hard-Problem
t = int(input())
for _ in range(t):
	m,a,b,c=map(int,input().split())
	if a>m or b>m:
		if a>m:
			a=m
		if b>m:
			b=m
	if (a+b+c)<=2*m:
		print(a+b+c)
	else:
		print(2*m)
