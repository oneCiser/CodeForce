from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

_n = inp()
ran = range(_n)
res = ['YES' for i in ran]
for _ in ran:
    cake = li()
    k = (cake[0] - 1)*cake[1] + (cake[1] - 1)
    if k != cake[2]:
        res[_] = 'NO'
[pr(_) for _ in res]
    
