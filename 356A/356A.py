from sys import stdout, stdin
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
import bisect
case = li()
ans=[0 for i in range(case[0])]
nextl=[i+1 for i in range(case[0]+2)]
for j in range(case[1]):
	f = li()
	i=f[0]
	while i<=f[1]:
		if ans[i-1]==0 and i!=f[2]:
			ans[i-1]=f[2]
		a=nextl[i]
		if i<f[2]:
			nextl[i]=f[2]
		else:
			nextl[i]=f[1]+1
		i=a
print(*ans)
