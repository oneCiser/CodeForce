from sys import stdout, stdin
import math
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

for _ in range(inp()):
    k = inp()
    pr(k%2050and-1or sum(map(int,str(k//2050))))