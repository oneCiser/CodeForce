from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
strp=lambda:stdin.readline().strip()
import re
p=re.compile('(?<=0)0(?=1)|(?<=1)0(?=0)')
for _ in[0]*inp():
 m=min(mp());s=f'0{strp()}0'
 while m:m-=1;s=p.sub('1',s)
 pr(s[1:-1])