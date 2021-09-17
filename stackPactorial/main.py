N=int(input())
L=[]
S=[]
k=1
ok=True
for i in range(N):
	x=int(input())
	while S==[] or x>S[-1]:
		L.append("+")
		S.append(k)
		k+=1
	if x==S[-1]:
		L.append('-')
		S.pop()
	elif x<S[-1]:
		ok=False
if ok:
	for i in L:
		print(i)
else:
	print('NO')