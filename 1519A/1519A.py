from sys import stdout, stdin
import math
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
_n = inp()
for _ in range(_n):
    r, b, d = mp()
    m = min(r,b)
    M = max(r,b)
    if abs(math.ceil(M/m) - 1) <= d:
        pr('YES')
    else:
        pr('NO')